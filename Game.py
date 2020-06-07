#!/usr/bin/env python3
"""
A text based shooter game (not really)
"""
import msvcrt
__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

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



#Begin game	
if __name__ == "__main__": start()
