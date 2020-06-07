#!/usr/bin/env python3
"""
A text based shooter game (not really)
"""

import msvcrt

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


gameRunning = True
stats = {
	"Health" : 0,
	"Attack_Damage" : 0,
	"Ranged_Damage" : 0,
	"Stamina" : 0
}

chatter = "\
###################\n\
###################\n\
###################"

def start():
	print(chatter)
	read()

def read():
	while gameRunning:
		input_char = msvcrt.getch()
		if input_char.upper() == 'W': pass
		if input_char.upper() == 'A': pass
		if input_char.upper() == 'S': pass
		if input_char.upper() == 'D': pass
		if input_char.upper() == 'X': exit()
		
	

#Begin game	
if __name__ == "__main__": start()
