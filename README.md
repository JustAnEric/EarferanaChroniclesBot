# EarferanaChroniclesBot
Earferana Chronicles Bot Repository to account for Replit's hosting changes. 
## How to update the bot's code on the server-side
- Edit the version file, first line to a newer version release number.
- Edit the other files, to propagate changes.
- Change the security.log file, to display all of your newer changes for the new version release number you added to the version file in this format: (edit version number and respective fields when commiting a new release)
```
[1.2.0]:
- Changed ... to resolve a conflict with the latest package releases
- Updated package name ... to be the latest release
- Edited the Earferana Chronicles Bot website
```
Everything will automatically update on the server after this commit.

## Run this bot on any server
### Grabbing the actual bot token
To grab the actual bot token for the Earferana Chronicles Bot, make sure you go [here](https://github.com/JustAnEric/EarferanaChroniclesBot/settings/secrets/actions) to see Repository Secrets. Find the secret named `TOKEN` and add it to your code **(LOCALLY)**
