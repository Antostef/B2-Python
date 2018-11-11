#!/usr/local/bin/python3
# 1b-dic.py
# Takes input of n str; returns array of sorted str
# Stefanaggi Antoine-Dominique
# 15/10/18

# Regex support library
import re

names=[]
userInput= input('Enter a name: ')

# Here we check if the string passed is conform to a name with a simple RegEx
# Returns a boolean
def is_good(str):
    if re.match(r"[a-zA-Z][^#&<>\"~;$^%{}?]", str) is not None:
        return True
    else:
        return False

# Code body
while userInput != 'q':
    while is_good(userInput) != True:
        userInput = input('Please enter a valid name: ')
    names.append(userInput)
    userInput = input()

# User's view
print(sorted(names))