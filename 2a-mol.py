#!/usr/local/bin/python3
# 2a-mol.py
# More or less game which plays through a file
# Stefanaggi Antoine-Dominique
# 23/10/18
import random

# initialization 
f   = open("play.vi", "r+")

f.write("Entre un nombre entier")

boolWon         = False
randomNumber    = random.randint(0,100)


# functions 

# Main game function 
def play(usrInput, rand):
    if (rand > usrInput):
        f.write("Plus grand")
    if (rand < usrInput):
        f.write("Plus petit")
    if (rand == usrInput):
        boolWon = True

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

# infinite loop
while boolWon != True:
    if is_number(f.read()):
        play(int(f.read()), randomNumber)
    else:
        if f.read() == "Plus grand":
            continue
        elif f.read() == "Plus petit":
            continue
        elif f.read() == "Entrez un nombre entier":
            continue
        else:
            f.write("Entrez un nombre entier")
    

# Game end
f.write("Bien joué vous avez gagné la réponse était", randomNumber)

