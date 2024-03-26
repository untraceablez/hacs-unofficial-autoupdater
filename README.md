# HACS Unofficial Autoupdater - Automatic Update Management for Home Assistant
Have you ever gone a bit without checking HACS for integration updates, just to be greeted by a dozen integrations that individually need updating? If so, this is the app for you. 

The HACS Unofficial Autoupdater will check all of your installed integrations, (including itself) for updates, apply the updates, and then restart Home Assistant. 

## Features:

* Automatic daily update checks for HACS and HACS integrations.
* Seamless update installation for HACS and integrations.
* Automatic backup of your configuration *before* updates.
* Restarts Home Assistant after applying updates (configurable).

## Requirements:

* Home Assistant
* HACS integration installed in Home Assistant
* Home Assistant Supervisor (*required for the backup functionality.*)


## Installation:

Install the App in HACS:

Within Home Assistant, navigate to the "HACS" section.
Click "Explore & Download Repositories".
Search for "HACS Unofficial Autoupdater".
Install the "HACS Unofficial Autoupdater" integration.

## Customization

interval: Controls how often the app checks for updates (default: 24 hours).
restart_home_assistant: Enables/disables automatic Home Assistant restart after updates (default: enabled).
Customization:

You can modify the interval in apps.yaml to adjust update check frequency.
The code can be further customized to send notifications or handle specific scenarios.
Important Notes:

## Backup: Configuring Backups
