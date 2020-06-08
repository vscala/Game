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
['#', '#', '#', '#'],\
['#', '#', '#', '#'],\
['#', '#', '#', '#']\
]

#character class for controllable character and npcs(?)
class character:
	def __init__(self, x, y, symbol):
		self.x = x
		self.y = y
		self.symbol = symbol
		map[x][y] = symbol

	def moveUp(self):
		if self.x - 1 >= 0:
			map[self.x][self.y] = '#'
			self.x = self.x - 1
			map[self.x][self.y] = self.symbol

	def moveLeft(self):
		if self.y - 1 >= 0:
			map[self.x][self.y] = '#'
			self.y = self.y - 1 
			map[self.x][self.y] = self.symbol

	def moveRight(self):
		if self.y + 1 < 4:
			map[self.x][self.y] = '#'
			self.y = self.y + 1
			map[self.x][self.y] = self.symbol

	def moveDown(self):
		if self.x + 1 < 4:
			map[self.x][self.y] = '#'
			self.x = self.x + 1
			map[self.x][self.y] = self.symbol		


gameRunning = True

#Print current map state
def displayMap():
	for row in map: print("".join(row))
	print('\n')

#Start Actions
def moveW(character):
	character.moveUp()
def moveA(character):
	character.moveLeft()
def moveS(character):
	character.moveDown()
def moveD(character):
	character.moveRight()
def stopGame(character):
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
	mainChar = character(0,0, "&")
	displayMap()
	read(mainChar)

#Read in player input
def read(character):
	global gameRunning
	while gameRunning:
		input_char = str(msvcrt.getch())[2]
		if input_char.upper() in actions: actions[input_char.upper()](character)
		displayMap()

#Call start function
if __name__ == "__main__": start()
