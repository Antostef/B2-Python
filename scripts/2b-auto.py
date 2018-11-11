#!/usr/local/bin/python3
# 2b-auto.py
# Script that plays the more or less game
# Stefanaggi Antoine-Dominique
# 10/11/18
import time

# functions
# simple function to read the play.vi file
def read_file():
    f = open("play.vi", "r")
    content = f.read()
    f.close()

    return (content)

# set the brackets to be closer to the wanted number | writes the guessed numbed in the play.vi file
def write_file(file_content):
    global lower_bracket
    global higher_bracket
    f = open("play.vi", "w")

    if file_content == "Less":
        higher_bracket = guess_number()
        f.write(str(guess_number()))
    elif file_content == "More":
        lower_bracket = guess_number()
        f.write(str(guess_number()))
    elif file_content == "Entrez un nombre entier":
        f.write(str(guess_number()))

    f.close()
    time.sleep(3)

# returns an int() that will be the next guess
def guess_number():

    return int((lower_bracket+higher_bracket)/2)

# initialising
boolWon = False
lower_bracket = 0
higher_bracket = 100

# script loop
while boolWon != True:
    file_content = read_file()

    if file_content == "Less" or file_content == "More" or file_content == "Entrez un nombre entier":
        write_file(file_content)
    elif file_content == "You won":
        print("Vous avez gagné")
        break
    else:
        time.sleep(1.5)