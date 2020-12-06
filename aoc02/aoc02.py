#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

passwords = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    passwords.append(line)
inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

validPasswords = 0
for p in passwords:
    m = re.search('^(\d+)-(\d+) (\w): (\w*)$', p)
    minChar = int(m.group(1))
    maxChar = int(m.group(2))
    checkChar = m.group(3)
    password  = m.group(4)
    passArray = list(password)

    charCnt = 0
    for c in passArray:
        if c is checkChar:
            charCnt+=1

    if charCnt >= minChar and charCnt <= maxChar:
        validPasswords += 1
    
print(f'Num Valid Passwords = {validPasswords }')

print("------------------")
print("---- PART 2 ------")
print("------------------")
validPasswords = 0
for p in passwords:
    m = re.search('^(\d+)-(\d+) (\w): (\w*)$', p)
    posOne = int(m.group(1))
    posTwo = int(m.group(2))
    checkChar = m.group(3)
    password  = m.group(4)
    passArray = list(password)

    if (passArray[posOne-1] == checkChar) != (passArray[posTwo-1] == checkChar):
        validPasswords += 1
    
print(f'Num Valid Passwords = {validPasswords }')


