#!/usr/local/bin/python3
# 2a-mol.py
# More or less game which plays through a file
# Stefanaggi Antoine-Dominique
# 23/10/18
import random
import time

# functions 
# Main game function | compares what the user put into the file with the random number, then calls the write_file
# with the respecting argument
def play(usrInput, rand):
    if (rand > usrInput):
        write_file(1)
    elif (rand < usrInput):
        write_file(2)
    else:
        write_file(3)

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

# functions that writes a different statement depending on the number passed by the function play()
def write_file(i):
    f = open("play.vi", "w")

    if i == 0:
        f.write("Entrez un nombre entier")
    elif i == 1:
        f.write("More")
    elif i == 2:
        f.write("Less")
    elif i == 3:
        f.write("You won")   
    f.close()
    time.sleep(2)

# Simple function that reads the play.vi file
def read_file():
    f = open("play.vi", "r")
    content = f.read()
    f.close()
    return (content)

# initialising
boolWon         = False
randomNumber    = random.randint(0,100)
write_file(0)

# infinite loop
while boolWon != True:
    userInput = read_file()
    
    if is_number(userInput):
        play(int(userInput), randomNumber)
    else:
        if userInput == "More" or userInput == "Less" or userInput == "Entrez un nombre entier":
            time.sleep(2)
        elif userInput == "You won":
            boolWon = True
        else:
            write_file(0)
    

# Game end
print("Bien joué vous avez gagné la réponse était", randomNumber)
