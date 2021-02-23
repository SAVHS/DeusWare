# -*- coding: utf-8 -*-
# filename          : invintory.py
# description       : Helper functions for the main.py file
# author            : Ian Ault
# email             : ian.ault@isd282.org
# date              : 02-23-2021
# version           : v1.1
# usage             : python main.py
# notes             : This file should not be run directly
# license           : MIT
# py version        : 3.7.8 (must run on 3.6 or higher)
#==============================================================================
import os


def highlight_selected(msg, selected):
	invintory = []
	for count, item in enumerate(msg):
		while selected+1 > len(msg):
			msg.append(" ")
	for count,item in enumerate(msg):
		if count == selected:
			item = f"\033[1;47m\033[1;30m{item}\033[1;m\033[1;m"
		invintory.append(item)
	return invintory

def format_menu(msg, width):
	msg = "|".join(msg)
	msg = f"|{msg}|"
	for count, char in enumerate(msg):
		try:
			if (msg[count-1] == "|" and msg[count+1] == "|") or (char == "|" and msg[count-1] != "|" and msg[count+1] != "|"):
				char = f"\033[4m{char}\033[0m"
		except IndexError:
			pass
		finally:
			print(char, end="")
	print()

def chunk(msg, size):
	final = []
	temp = []
	for count, item in enumerate(msg):
		done = False
		temp.append(item)
		if (count+1) % size == 0:
			final.append(temp)
			temp = []
			done = True
	if not done:
		final.append(temp)
	return final

def menu(dimensions, msg):
	width, height = dimensions
	msg = chunk(msg.split() if "list" not in str(type(msg)) else msg, width)
	inv_list = []
	for section in msg:
		while len(section) < width:
			section.append(" ")
		inv_list.append(section)
		
	print(" "+"_"*int(width*2-1))
	for column in range(height):
		try:
			format_menu(inv_list[column], width)
		except IndexError:
			format_menu([" "]*width, width)

if __name__ == "__main__":
	print("Wrong module, switchihng to \"main.py\"...")
	os.system("python main.py")
