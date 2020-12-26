#!/usr/bin/python

import math
import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
cardKey = int(inputFile.readline().strip())
doorKey = int(inputFile.readline().strip())
inputFile.close()

print(f'Card Key = {cardKey}')
print(f'Door Key = {doorKey}')
def genKey(subjNum, loops):
    val = 1
    for i in range(loops):
        val = (val * subjNum) % 20201227

    return val

print("------------------")
print("---- PART 1 ------")
print("------------------")
prime = 20201227

if False: # too slow
    doorLoops = 1
    while (7**doorLoops) % prime != doorKey: doorLoops+=1

    cardLoops = 1
    while (7**cardLoops) % prime != cardKey: cardLoops+=1

    print(f'Card Loops = {cardLoops}')
    print(f'Door Loops = {doorLoops}')

lastVal=1

numExps = math.floor(math.log(prime,2))
multiples = [1, 7]
print(numExps+1)
for i in range(2,numExps+10):
    print(f'{i} = {multiples[i-1]}^2 = ', end='')
    multiples.append((multiples[i-1]*multiples[i-1]) % prime)
    print(f'{multiples[-1]}')

print(multiples)

# Find Card Loops
cardLoops = 0
for exp in range(prime):
    #print("----------------------")
    if exp%50000 == 0: print(f'exp = {exp}')
    val = 1 
    shift = 0
    while exp >> shift != 0:
        if ((exp >> shift) & 1) == 1:
            #print(f'{shift}')
            val *= multiples[shift+1]

        shift += 1

    #print(f'{(7**exp) % prime} == {val % prime}')

    if val % prime == cardKey:
        cardLoops = exp
        print(f'CardLoops: exp={exp} val={val}')
        break

doorLoops = 0
for exp in range(prime):
    #print("----------------------")
    if exp%50000 == 0: print(f'exp = {exp}')
    val = 1 
    shift = 0
    while exp >> shift != 0:
        if ((exp >> shift) & 1) == 1:
            #print(f'{shift}')
            val *= multiples[shift+1]

        shift += 1

    #print(f'{(7**exp) % prime} == {val % prime}')

    if val % prime == doorKey:
        doorLoops = exp
        print(f'DoorLoops: exp={exp} val={val}')
        break

print(f'Encryption Key (via Card) = {genKey(cardKey, doorLoops)}')
print(f'Encryption Key (via Door) = {genKey(doorKey, cardLoops)}')

print("------------------")
print("---- PART 2 ------")
print("------------------")


