import os
import psutil
import time
import subprocess
import keyboard

os.system('title Femboy Discord Killer')


# Replace with the actual path to your Discord.exe here
DISCORD_PATH = "C:\\Users\\Admin\\AppData\\Local\\Discord\\app-1.0.9166\\Discord.exe"
# Replace with the actual trigger button here
TRIGGER_BUTTON = ('ctrl+alt+]')
# Replace with the actual sleeping time before reconnecting to the call
SLEEPING_TIME = 10
# Replace with the actual reconnect button
RECONNECT_BUTTON = 'F13'
# Replace with the actual sleep after closing Discord time
KILLED_APP_SLEEPING_TIME = 2

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
    print(f"Press \" \033[4m{TRIGGER_BUTTON.title()}\033[0m \" to reboot Discord.\n")
    print(f"Sleeping time before reconnecting to the call is: {SLEEPING_TIME}.\n")
    print(f"Your Discord reconnect button is: {RECONNECT_BUTTON}.\n")
    print(f"Your Discord path is: {DISCORD_PATH}.\n")
    print(f"\n{cat_line}\n")

greeting_message()

# Find and kill the Discord process
def close_discord():
    for proc in psutil.process_iter():
        if proc.name() == "Discord.exe":
            proc.kill()

# Opens new Discord.exe
def open_discord():
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen([DISCORD_PATH], stdout=devnull, stderr=devnull)

# Reconnects to an old call using your own Discord bind
def reconnect_to_call():
    # Wait for Discord to fully load (Adjust the time as necessary)
    time.sleep(SLEEPING_TIME)

    # Simulate pressing necessary keys to reconnect to the last call
    keyboard.press_and_release(RECONNECT_BUTTON)

# Main body, kinda
def restart_discord():
    global restart_count
    restart_count += 1
    console_clear()

    print(f"\n{cat_line}\n")
    print("☠️ Closing Discord.exe...\n")
    close_discord()
    print(f"😴 Sleeping for {KILLED_APP_SLEEPING_TIME} seconds...\n")
    time.sleep(KILLED_APP_SLEEPING_TIME)
    print("🎃 Opening Discord.exe...\n")
    open_discord()
    print(f"😴 Sleeping for {SLEEPING_TIME} seconds...\n")
    reconnect_to_call()
    print("🥳 Reconnected to the voice channel. Sleeping for 5 seconds before restarting.")
    time.sleep(5)
    console_clear()
    greeting_message()


keyboard.add_hotkey(TRIGGER_BUTTON, restart_discord)
keyboard.wait()