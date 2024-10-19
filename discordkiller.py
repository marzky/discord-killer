import os
from psutil import process_iter
from time import sleep
from subprocess import Popen
from keyboard import wait, press_and_release, add_hotkey
from json import load

os.system('title Femboy Discord Killer')
with open('femboy_config.json', 'r') as config_file:
    config = load(config_file)


DISCORD_PATH = config["DISCORD_PATH"]
TRIGGER_HOTKEY = config["TRIGGER_HOTKEY"]
SLEEPING_TIME = config["SLEEPING_TIME"]
RECONNECT_KEY = config["RECONNECT_KEY"]
KILLED_APP_SLEEPING_TIME = config["KILLED_APP_SLEEPING_TIME"]

console_clear = lambda: os.system('cls')
restart_count = 0
cat_line = "😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀"

def greeting_message():
    print(f"\n{cat_line}\n")
    print("\tOmagaa hiiiyaa!! I am \033[36mDISCORD\033[0m \033[31mKILLER\033[0m, \033[35mnya!\033[0m 🥰")
    if restart_count != 0:
        print(f"\t  \033[32mSuccesfully re-opened Discord {restart_count} time(s)!\033[0m\n")
    else:
        print("")
    print(f"Press \" \033[4m{TRIGGER_HOTKEY.title()}\033[0m \" to reboot Discord.\n")
    print(f"Sleeping time before reconnecting to the call is: {SLEEPING_TIME}.\n")
    print(f"Your Discord reconnect button is: {RECONNECT_KEY}.\n")
    print(f"Your Discord path is: {DISCORD_PATH}.\n")
    print(f"\n{cat_line}\n")

greeting_message()

# Find and kill the Discord process
def close_discord():
    for proc in process_iter():
        if proc.name() == "Discord.exe":
            proc.kill()

# Opens new Discord.exe
def open_discord():
    with open(os.devnull, 'w') as devnull:
        Popen([DISCORD_PATH], stdout=devnull, stderr=devnull)

# Reconnects to an old call using your own Discord bind
def reconnect_to_call():
    # Wait for Discord to fully load (Adjust the time as necessary)
    sleep(SLEEPING_TIME)

    # Simulate pressing necessary keys to reconnect to the last call
    press_and_release(RECONNECT_KEY)

# Main body, kinda
def restart_discord():
    global restart_count
    restart_count += 1
    console_clear()

    print(f"\n{cat_line}\n")
    print("☠️ Closing Discord.exe...\n")
    close_discord()
    print(f"😴 Sleeping for {KILLED_APP_SLEEPING_TIME} seconds...\n")
    sleep(KILLED_APP_SLEEPING_TIME)
    print("🎃 Opening Discord.exe...\n")
    open_discord()
    print(f"😴 Sleeping for {SLEEPING_TIME} seconds...\n")
    reconnect_to_call()
    print("🥳 Reconnected to the voice channel. Sleeping for 5 seconds before restarting.")
    sleep(5)
    console_clear()
    greeting_message()


add_hotkey(TRIGGER_HOTKEY, restart_discord)
wait()