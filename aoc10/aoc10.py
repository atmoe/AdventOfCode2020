#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

adaptors = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    adaptors.append(int(line))

inputFile.close()


dbgPrint(adaptors)

adaptors.sort()

print("------------------")
print("---- PART 1 ------")
print("------------------")
maxVal = max(adaptors)
lastVal = 0
diff1 = 0
diff3 = 0
for a in adaptors:
    if a-lastVal == 1: diff1+=1
    if a-lastVal == 3: diff3+=1
    lastVal = a

diff3+=1 # for device

print(f'Result = {diff1*diff3}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

deltaVals = []

lastVal = 0
for a in adaptors:
    deltaVals.append(a-lastVal)
    lastVal = a

deltaVals.append(3)
dbgPrint(deltaVals)


# each delta of 3 is a discontinuity 
#   count number of delta of 1 between delta of 3s, there are a fixed
#   number of permutations for a run of ones.  The code below doesnt work
#   if the run of ones is greater than 4.  Permutations were calculated
#   brute force by hand
cum = 1
numOnes = 0
for v in deltaVals:
    if v == 1: 
        numOnes += 1
        continue
    elif v == 3:
        if numOnes == 0: permutations = 1
        if numOnes == 1: permutations = 1
        if numOnes == 2: permutations = 2
        if numOnes == 3: permutations = 4
        if numOnes == 4: permutations = 7
        cum *= permutations
        numOnes=0

print(f'Total Combinations = {cum}')

