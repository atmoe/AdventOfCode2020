#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
earliestDepart = int(inputFile.readline())
buslines = inputFile.readline().strip().split(',')
inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

busses     = []
for idx,b in enumerate(buslines):
    if b != 'x':
        busses.append(int(b))

currentSim = []
for idx,b in enumerate(busses):
    currentSim.append([0, idx])

print(earliestDepart)
print(busses)
print(currentSim)

while currentSim[0][0] < earliestDepart:
    currentSim[0][0] += busses[currentSim[0][1]]
    currentSim.sort()
    dbgPrint(currentSim)

waitTime = currentSim[0][0] - earliestDepart

print(f"bus line = {busses[currentSim[0][1]] * waitTime}")

print("------------------")
print("---- PART 2 ------")
print("------------------")

#################################
#### This works, but is slow ####
if False: 
    timestampFound = 0
    maxVal    = 0
    maxValIdx = 0
    for idx,b in enumerate(buslines):
        if b == 'x': continue
        if int(b) > maxVal: 
            maxValIdx = idx
            maxVal = int(b)

    currTimeStamp = maxVal


    while not timestampFound:
        timestampFound = True
        for idx,b in enumerate(buslines):
            if b == 'x': continue

            if ((currTimeStamp - maxValIdx) + idx) % int(b) != 0:
                timestampFound = False
                break

        if not timestampFound:
            currTimeStamp += maxVal
    print(f"Time Stamp = {currTimeStamp-maxValIdx}")
#################################

#############################
### Fast Implementation 
busList = []
for idx,b in enumerate(buslines):
    if b != 'x':
        busList.append([int(b), idx])

print(busList)

# This essentially keeps a running increment value
# Find when a run of 1, 2, 3, ... occurs then remember
# that increment to find the run for the next number.

incr = 1
val = 1
for b in busList:
    # increment til run found
    while (val + b[1]) % b[0] != 0:
        val += incr

    # After run found, it will repeat
    incr *= b[0]

print(f'Value = {val}')
