# Discord application killer script
This script restarts Discord application with the user-chosen hotkey and then connects one to the user-chosen voice channel.
This script might help if for some reason user needs to manually restart Discord and reconnect to the voice channel often.

## JSON-file configuration
### "DISCORD_PATH": "path\\to\\your\\discord\\in\\this\\format\\Discord.exe",
Allows you to change your Discord application path.
> [!IMPORTANT]
> Don't forget to leave "Discord.exe" by the end of your path.

### "TRIGGER_BUTTON": "ctrl+alt+]",
Allows you to change your script-triggering hotkey.
> [!TIP]
> Examples: "r", "h+y", "alt+ctrl+k".

### "SLEEPING_TIME": 10,
Allows you to change the time script will spend sleeping after it initialized Discord application launching.
> [!NOTE]
> Only adjust if your Discord application launches significantly faster or slower than the default value.

### "RECONNECT_BUTTON": "F13",
Allows you to change the virtual key used for Discord voice channel reconnection shortcut.
> [!NOTE]
> Only adjust if your keyboard actually have F13 key. Adjusting will also impact fakekeypusher.py script.

### "KILLED_APP_SLEEPING_TIME": 2
Allows you to change the time script will spend sleeping after killing your Discord application.
> [!NOTE]
> Only adjust if your Discord application takes more time to shut down than the default value.
