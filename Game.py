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

map = [\
['#', '#', '#', '#'],\
['#', ' ', ' ', '#'],\
['#', ' ', ' ', '#'],\
['#', '#', '#', '#']\
]

gameRunning = True

#Print current map state
def displayMap():
	for row in map: print("".join(row))

#Start Actions
def moveW():
	pass
def moveA():
	pass
def moveS():
	pass
def moveD():
	pass
def stopGame():
	global gameRunning
	gameRunning = False
#End Actions

#Hashtable key-to-action
actions = {
	"W": moveW,
	"A": moveA,
	"S": moveS,
	"D": moveD,
	"X": stopGame
}

#Game starts here
def start():
	displayMap()
	read()

#Read in player input
def read():
	global gameRunning
	while gameRunning:
		input_char = str(msvcrt.getch())[2]
		if input_char.upper() in actions: actions[input_char.upper()]()

#Call start function
if __name__ == "__main__": start()
