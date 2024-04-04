# HACS Unofficial Autoupdater - Automatic Update Management for Home Assistant

Have you ever gone a bit without checking HACS for integration updates, just to be greeted by a dozen integrations that individually need updating? If so, this is the app for you.

The HACS Unofficial Autoupdater will check all of your installed integrations, (including itself) for updates, apply the updates, and then restart Home Assistant.

## Features

* Automatic daily update checks for HACS and HACS integrations.
* Seamless update installation for HACS and integrations.
* Automatic backup of your configuration *before* updates.
* Restarts Home Assistant after applying updates (configurable).

## Requirements  

* Home Assistant
* HACS integration installed in Home Assistant (Installation instructions can be found [here.](https://hacs.xyz/))
* Home Assistant Supervisor (*required for the backup functionality.*)

## Installation

Install the App in HACS:

Within Home Assistant, navigate to the "HACS" section.
Click "Explore & Download Repositories".
Search for "HACS Unofficial Autoupdater".
Install the "HACS Unofficial Autoupdater" integration.

## Customization

You can customize both the update check interval and the backup interval by defining them in the `apps.yaml` file. They are the values `update_interval` and `backup_interval`. They are both set in seconds. These are the default values:

```yaml
  update_interval: 86400
  backup_interval: 3600 
```  

Test