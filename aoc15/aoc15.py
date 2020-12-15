#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
startingNumbers = [int(i) for i in inputFile.readline().strip().split(',')]
inputFile.close()

print(startingNumbers)

print("------------------")
print("---- PART 1 ------")
print("------------------")
numbers = []
for n in startingNumbers:
    numbers.append(n)

numTurns = 2020
for i in range(numTurns):
    if i < len(startingNumbers):
        dbgPrint(f'turn {i+1} = {numbers[i]}')
    else:
        lastNum  = numbers[-1]
        lastSeen = -1
        for n in range(len(numbers)-2, -1, -1):
            if numbers[n] == lastNum:
                lastSeen=n
                break
        if lastSeen == -1:
            numbers.append(0)
        else:
            numbers.append(i-1-lastSeen)

        dbgPrint(f'turn {i+1} = {numbers[-1]}')

print(f'turn {i+1} = {numbers[-1]}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
lastIdx = {}
numbers = []
for idx,n in enumerate(startingNumbers[0:-1]):
    numbers.append(n)
    lastIdx[n] = idx

numTurns = 30000000 
lastNum = startingNumbers[-1]
for i in range(numTurns):
    if i < len(startingNumbers)-1:
        dbgPrint(f'turn = {i+1} = {numbers[i]}')
    elif i == len(startingNumbers)-1:
        dbgPrint(f'turn = {i+1} = {lastNum}')
    else:
        nextNum = -1
        if not lastNum in lastIdx.keys():
            nextNum = 0
        else:
            nextNum = (i - 1 - lastIdx[lastNum])

        lastIdx[lastNum] = i-1
        lastNum = nextNum

        if i % 1000000 ==0 :
            dbgPrint(f'turn = {i+1} = {lastNum}')

print(f'turn {i+1} = {lastNum}')


