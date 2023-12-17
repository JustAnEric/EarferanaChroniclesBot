# ONLY FOR USE ON SERVERS ONLY! #
## This file propagates changes from this repository and updates them on the server-side.
### A normal user does not need to run this, as this file would be viewed as completely useless as the bot already runs on a server!

# If you are an average collaborator on this project, you're not allowed to modify, delete, or distribute the following software you see in front of your eyes. #
# : Even though there is a GNU License, this file is not for some average joe to mess around with. This file contains sensitive data.

# ⚠️ LAST WARNING ⚠️ #

from .github import (
  Repository
)
from threading import (
  Thread
)
import bot

current_version = open('./version').readline()
repo = Repository("https://github.com/JustAnEric/EarferanaChroniclesBot") #initialise repository
app = bot.BotApplication
is_paused=False

def run_app():
  global is_paused
  bota = app()
  if is_paused:
    print("[-] Pausing...")
    print("[*] Waiting to resume.")
    while is_paused:pass
    print("[-] Starting new bot instance.")
    bota.logout()
    importlib.reload(bot)
    print("[*] Reloaded modules successfully.")
    print("[-] Going online again...")
    app = bot.BotApplication
    bota = app()
    
if repo.get_version() == current_version:
  # latest version/release.
  print("Latest version/release. Starting software in a new thread.")
  _e = Thread(target=run_app, daemon=True) # start from a completely different host/parent
  _e.start()
  print("Latest version checker has started.")
else:
  # update the software.
  print(f"Updating to version {repo.get_version()}...")
  repo.current_folder.update_files(["main.py", "db.json", "version"]) # (*queries)
  print(f"Successfully updated. Latest version is {repo.get_version()}")
  print("Starting software in a new thread.")
  _e = Thread(target=run_app, daemon=True) # start from a completely different host/parent
  _e.start()
  print("Latest version checker process has started.")
  current_version = repo.get_version()

while True:
  if repo.get_version() == current_version:
    pass
  else:
    print("[*] Detected new version.")
    print("[-] Stopping bot process...")
    
    print(f"Updating to version {repo.get_version()}...")
    repo.current_folder.update_files(["main.py", "db.json", "version"]) # (*queries)
    print(f"Successfully updated. Latest version is {repo.get_version()}")
    current_version = repo.get_version()

    is_paused=True
    print("[{UPDATER*1.0.0}] STARTING NEW VERSION...")
