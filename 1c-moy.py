#!/usr/local/bin/python3 
# 1c-moy.py
# Takes input of n str and float; returns average and top 5
# Stefanaggi Antoine-Dominique
# 16/10/18

# Regex support library
import re

bulletin = []
strName = 'name'
strGrade = 'grade'
cpt = 0
tot = 0

userInput = input('Student\'s name and grade: ')

# Here we check if the value passed can be turned into a float and if it is under 20.0
# Returns a boolean
def is_number(s):
    try:
        float(s)
        if float(s)<=20.0:
            return True
        else:
            return False
    except ValueError:
        return False

# Here we check if the string passed is conform to a name with a simple RegEx
# Returns a boolean
def is_good(str):
    if re.match(r"[a-zA-Z][^#&<>\"~;$^%{}?]", str) is not None:
        return True
    else:
        return False

# Code body
while userInput != 'q':
    var1, var2 = userInput.split(' ')

    while is_good(var1) != True:
        var1 = input('Please enter a valid name: ')

    while is_number(var2) != True:
        var2 = input('Please enter a valid number between 20 and 0: ')

    bulletin.append({strName: var1, strGrade: float(var2)})
    tot += float(var2)
    cpt += 1
    userInput = input('Student\'s name and grade: ')

bestStudent = sorted(bulletin, key=lambda k: k['grade'], reverse=True)

# User's view
print ('The average is:',tot/cpt)
if cpt >= 5:
    for i in range(0, 5):
        print (bestStudent[i])
else:
    for student in bestStudent:
        print(student)