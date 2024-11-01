import os
from psutil import process_iter
from time import sleep
from subprocess import Popen
from keyboard import wait, press_and_release, add_hotkey
from json import load
from win32gui import (IsWindowVisible, GetWindowText, EnumWindows,
                      SetWindowPos, ShowWindow, SetForegroundWindow)
from win32con import (HWND_TOP, SWP_NOZORDER, SWP_SHOWWINDOW, SW_HIDE,
                      SW_MAXIMIZE)

with open('femboy_config.json', 'r') as config_file:
    config = load(config_file)

DISCORD_PATH = config["DISCORD_PATH"]
TRIGGER_HOTKEY = config["TRIGGER_HOTKEY"]
SLEEPING_TIME = config["SLEEPING_TIME"]
RECONNECT_KEY = config["RECONNECT_KEY"]
KILLED_APP_SLEEPING_TIME = config["KILLED_APP_SLEEPING_TIME"]
MONITOR_SIDE = config["MONITOR_SIDE"]
USER_SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
USER_SCREEN_WIDTH = config["SCREEN_WIDTH"]
SWITCHING_MONITORS = config["SWITCHING_MONITORS"]

gui_monitor_side = ""
if MONITOR_SIDE == "left":
    gui_monitor_side = "left"
else:
    gui_monitor_side = "right"

restart_count = 0
cat_line = "😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀😸😻😼🙀"


def greeting_message():
    print(f"\n{cat_line}\n")
    print("\tOmagaa hiiiyaa!! I am \033[36mDISCORD\033[0m \033[31mKILLER\033[0m, \033[35mnya!\033[0m 🥰")
    if restart_count:
        print(f"\t  \033[32mSuccessfully re-opened Discord {restart_count} time(s)!\033[0m\n")
    else:
        print("")
    print(f"Press \" \033[4m{TRIGGER_HOTKEY.title()}\033[0m \" to reboot Discord.\n")
    print(f"Sleeping time before reconnecting to the call is: {SLEEPING_TIME}.\n")
    print(f"Your Discord reconnect button is: {RECONNECT_KEY}.\n")
    print(f"Your Discord path is: {DISCORD_PATH}.\n")
    if SWITCHING_MONITORS:
        print(f"Script will switch Discord window to the monitor on the: "
              f"{gui_monitor_side}.\n")
    print(f"\n{cat_line}\n")


greeting_message()


def close_discord():
    for proc in process_iter():
        if proc.name() == "Discord.exe":
            proc.kill()


def open_discord():
    with open(os.devnull, 'w') as devnull:
        Popen([DISCORD_PATH], stdout=devnull, stderr=devnull)


def find_discord_window():
    def callback(hwnd, found_windows):
        if IsWindowVisible(hwnd) and "Discord" in GetWindowText(hwnd):
            found_windows.append(hwnd)
    windows = []
    EnumWindows(callback, windows)
    return windows[0] if windows else None


def move_discord_to_secondary_monitor():
    try:
        hwnd = find_discord_window()
        if hwnd:
            screen_width, screen_height = USER_SCREEN_WIDTH, USER_SCREEN_HEIGHT
            if MONITOR_SIDE == "left":
                x_offset = -screen_width
            else:
                x_offset = screen_width
            SetWindowPos(hwnd, HWND_TOP, x_offset, 0, screen_width, screen_height, SWP_NOZORDER | SWP_SHOWWINDOW)
            ShowWindow(hwnd, SW_HIDE)
            ShowWindow(hwnd, SW_MAXIMIZE)
            SetForegroundWindow(hwnd)
        else:
            print("Discord window not found.")
    except Exception as e:
        print(f"Error moving Discord window: {e}")


def reconnect_to_call():
    sleep(SLEEPING_TIME)
    press_and_release(RECONNECT_KEY)


def restart_discord():
    global restart_count
    restart_count += 1
    os.system('cls')

    print(f"\n{cat_line}\n")
    print("☠️ Closing Discord.exe...\n")
    close_discord()
    print(f"😴 Sleeping for {KILLED_APP_SLEEPING_TIME} seconds...\n")
    sleep(KILLED_APP_SLEEPING_TIME)
    print("🎃 Opening Discord.exe...\n")
    open_discord()
    print(f"😴 Sleeping for {SLEEPING_TIME} seconds...\n")
    reconnect_to_call()
    print("🥳 Reconnected to the voice channel.\n")
    if SWITCHING_MONITORS:
        move_discord_to_secondary_monitor()
        print("📺 Switched to the secondary monitor.\n")
    print("😴 Sleeping for 5 seconds before restarting.\n")
    sleep(5)
    os.system('cls')
    greeting_message()


add_hotkey(TRIGGER_HOTKEY, restart_discord)
wait()
