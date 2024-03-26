import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

class HACSAutoUpdater(hass.Hass):

    def initialize(self):
        # Get configuration values (with defaults)
        self.update_interval = self.args.get("update_interval", 86400) 
        self.backup_interval = self.args.get("backup_interval", 3600)

        # Schedule initial update with a slight delay
        initial_update = datetime.now() + timedelta(seconds=10)
        self.run_daily(self.check_and_update, initial_update)

        # Schedule backups based on backup_interval 
        initial_backup = datetime.now() + timedelta(seconds=30)  # Adjust offset if needed
        self.run_every(self.create_backup, initial_backup, self.backup_interval)

    def check_and_update(self, kwargs):
        # Check internet connectivity (Google DNS)
        if not self.check_connectivity("8.8.8.8"):
            self.log("HACS Autoupdater can't connect to the internet.")
            return
        
        # Create a backup before updating 
        backup_name = "hacs-autoupdater-" + datetime.now().strftime("%H-%M-%m-%d-%y")
        self.log(f"Creating backup: {backup_name}")

        try:
            self.call_service("hassio/snapshot/full", snapshot_name=backup_name)
        except Exception as e:  # Catch any potential exception
            self.log(f"Error: unable to create backup, stopping update process. ({e})")
            return  # Stop the update process

        broken_repos = []  # List to store unreachable repositories

        # Check for HACS updates
        hacs = self.get_app("HACS")
        if hacs.pending_update:
            self.log("HACS update available, updating...")
            hacs.update()

        # Check for updates to HACS integrations
        for repo in hacs.repositories:
            if repo.pending_update:
                self.log(f"{repo.display_name} update available, updating...")
                repo.update()

        # Handle broken repositories 
        if broken_repos:
            error_msg = "One or more repositories could not be reached. Their integrations have not been updated. You can find a list of the repositories here: /config/broken_repos.txt"
            error_file = "/config/broken_repos.txt"  # Adjust path as needed
            with open(error_file, "w") as f:
                f.write("\n".join(broken_repos))
            self.log(error_msg + error_file)
        
        def check_connectivity(self, host):
        try:
            socket.gethostbyname(host)
            return True
        except socket.gaierror:
            return False

        # Schedule restart if updates were applied
        if hacs.pending_restart:
            self.log("Updates applied, restarting Home Assistant in 1 minute")
            self.run_in(self.restart_ha, 60)

    def restart_ha(self, kwargs):
        self.call_service("homeassistant/restart")
