from pynput.keyboard import Key
from pynput import keyboard
from os import system
from time import sleep
import invintory


keyboard_controller = keyboard.Controller()
invintory_list = ["⛏","⚔","🛡","$","&","1","1","1","1","2","3","4","5","6"]


def clear():
	system("clear")
	
def on_release(key):
	if key:
		return(key)


if __name__ == "__main__":
	keyboard_listener = keyboard.Listener(on_release=on_release)
	keyboard_listener.start()
	while True:
		for i in range(36):
			clear()
			selected = i
			invintory.menu((9,4), invintory.highlight_selected(invintory_list, selected))
			sleep(0.3)
