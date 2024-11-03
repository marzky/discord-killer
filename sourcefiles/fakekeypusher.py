import keyboard
import time
import json

with open('femboy_config.json', 'r') as config_file:
    config = json.load(config_file)

RECONNECT_KEY = config["RECONNECT_KEY"]
time.sleep(7)
keyboard.press_and_release(RECONNECT_KEY)