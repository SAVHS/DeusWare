from pynput.keyboard import Key
from pynput import keyboard
from time import sleep


keyboard_controller = keyboard.Controller()
def on_release(key):
	if key:
		print(key)

keyboard_listener = keyboard.Listener(on_release=on_release)
keyboard_listener.start()


while True:
	sleep(1)
