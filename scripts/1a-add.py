#!/usr/local/bin/python3
# 1a-add.py
# Takes input of two float; returns the sum
# Stefanaggi Antoine-Dominique
# 15/10/18

inta = input('First number: ')
intb = input('Second number: ')

# Here we check if the value passed can be turned into a float
# Returns a boolean
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Code Body
while is_number(inta) != True:
    inta = input('Please put a number: ')

while is_number(intb) != True:
    intb = input('Please put a number: ')

# User's view
print(float(inta) + float(intb))
