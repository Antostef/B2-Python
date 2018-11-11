#!/usr/local/bin/python3
# 1d-mol.py
# More or less game
# Stefanaggi Antoine-Dominique
# 22/10/18
import random
import signal
import sys
import os

randomNumber = random.randint(0,100)

# Here we intercept a SIGINT, and SIGTERM to handle them gently
def ctrlc(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Are you not entertained ?\nOh and by the way the answer was", randomNumber," You newbie")
    
    sys.exit(0)

# Here we check that the user input is an int
def userInput(): 
    x = input("Please put a number: ")
    if x == 'q':
        return won(x)
    while is_number(x) != True:
        x = input(" Please put a number: ")
        if x == 'q':
            return won(x)
    play(int(x), randomNumber)

# Here we check if the value passed can be turned into an int and is between 0-100
# Returns a boolean
def is_number(s):
    try:
        int(s)
        if int(s) <= 100 and int(s) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Function which returns a statement if you won or if you quit with the solution
def won(char):
    if char == 'y':
        print("Bien joué vous avez gagné, la solution était: ", randomNumber)
    if char == 'q':
        print("L'abandon c'est pour les loser, la solution était: ", randomNumber)

# Main game function 
def play(usrInput, rand):
    if (rand > usrInput):
        print("Plus grand")
        userInput()
    if (rand < usrInput):
        print("Plus petit")
        userInput()
    if (rand == usrInput):
        won('y')

# Code body
signal.signal(signal.SIGINT, ctrlc)
signal.signal(signal.SIGTERM, ctrlc)
userInput()
