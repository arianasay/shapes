from turtle import *
#from random import randint
def square (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (4):
		speed (1)
		forward (length)
		right (90)
	end_fill ()
	
def triangle (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (3):
		speed (1)
		forward (length)
		right (120)
	end_fill ()
def hexagon (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (6):
		speed (1)
		forward (length)
		right (60)
	end_fill ()
def octagon (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (8):
		speed (1)
		forward (length)
		right (45)
	end_fill ()
def triacontakaihexagon (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (36):
		speed (1)
		forward (length)
		right (10)
	end_fill ()
def hexacontakaigon (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (60):
		speed (1)
		forward (length)
		right (6)
	end_fill ()
def Trictohexacontagon (color):
	#goto(randint, randint)
	fillcolor(color)
	begin_fill ()
	for i in range (360):
		speed (1)
		forward (length)
		right (1)
	end_fill ()
	
#*******************************************************************
interest = True
while interest == True:
	answer = input (" Choose a shape?(square/hexagon/triangle/octagon/triacontakaihexagon/hexacontakaigon/Trictohexacontagon)")
	colorChoice = input("choose a color.")
	size= input ("length?")
	length = int(size)
	if answer == "square":
		square (colorChoice)
	elif answer == "hexagon":
		hexagon (colorChoice)
	elif answer == "triangle":
		triangle (colorChoice)
	elif answer == "octagon":
		octagon(colorChoice)
	elif answer == "triacontakaihexagon":
		triacontakaihexagon(colorChoice)
	elif answer == "hexacontakaigon":
		hexacontakaigon(colorChoice)
	elif answer == "Trictohexacontagon":
		Trictohexacontagon(colorChoice)
	else :
		print("You stupid did you even read the directions, go back and try again!!!!")
	response = input("Would You Like To Play Again?")
	if response == "yes" or response == "Yes" or response == "Si" or response == "We":
		interest = True
	else :
		interest = False
	