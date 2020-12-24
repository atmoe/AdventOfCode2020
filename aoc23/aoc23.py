#!/usr/bin/python

import sys
import re
import copy
from collections import deque

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

testInput = [3, 8, 9, 1, 2, 5, 4, 6, 7]
officialInput = [5, 8, 3, 9, 7, 6, 2, 4, 1]

#cups = copy.deepcopy(testInput)
cups = copy.deepcopy(officialInput)
cupsLen = len(cups)

print("------------------")
print("---- PART 1 ------")
print("------------------")
currentCupIdx = 0
currentCupVal = cups[currentCupIdx]

for i in range(100):
    dbgPrint(f'--- Move {i+1} ---')
    dbgPrint(f' cups = {cups}  currCup = cups[{currentCupIdx}] = {currentCupVal}')

    destTarget = currentCupVal - 1

    pickedUp = []
    pickedUp.append(cups[(currentCupIdx+1) % cupsLen])
    pickedUp.append(cups[(currentCupIdx+2) % cupsLen])
    pickedUp.append(cups[(currentCupIdx+3) % cupsLen])
    
    for r in pickedUp:
        cups.remove(r)
    dbgPrint(f' picked = {pickedUp}')

    # current cup index now incorrect due to removal!

    maxCup = max(cups)
    dbgPrint(f' maxCup = {maxCup}')
    while not (destTarget in cups) and destTarget > 0: destTarget-=1
    if destTarget == 0:
        dest = maxCup
    else:
        dest = destTarget

    destIdx = cups.index(dest)
    dbgPrint(f' destination = {dest}')

    cups = cups[0:destIdx+1] + pickedUp + cups[destIdx+1:] 
    currentCupIdx = (cups.index(currentCupVal) + 1) % cupsLen
    currentCupVal = cups[currentCupIdx]

oneIdx = cups.index(1)
finalArr = cups[oneIdx+1:] + cups[0:oneIdx]
finalStr = "".join(str(x) for x in finalArr)

print(f'Final Cups = {cups}')
print(f'Final Str  = {finalStr}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
class Cup:
    def __init__(self, val):
        self.val = val
        self.next = None

cups = copy.deepcopy(testInput)
cups = copy.deepcopy(officialInput)

maxVal = 1000000
cupHash = {}
headPtr = None
lastPtr = None
for c in cups:
    newCup = Cup(c)
    if not headPtr:
        headPtr = newCup

    if lastPtr:
        lastPtr.next = newCup

    lastPtr = newCup
    cupHash[c] = newCup

for c in range(len(cups)+1, 1000001):
    newCup = Cup(c)
    lastPtr.next = newCup
    lastPtr = newCup
    cupHash[c] = newCup

# close loop
lastPtr.next = headPtr

print("List created")

currPtr = headPtr
for i in range(10000000):
    # extract 3 cups
    pickHead = currPtr.next
  
    pickVals = []
    pickVals.append(pickHead.val)
    pickTail = pickHead
    for i in range(2):
        pickTail = pickTail.next
        pickVals.append(pickTail.val)

    # remove from loop
    currPtr.next = pickTail.next
    
    pickVals.sort()
    destVal = currPtr.val - 1
    while destVal in pickVals: destVal -= 1
    if destVal == 0:
        destVal = maxVal
        while destVal in pickVals: destVal -= 1


    # insert cups after destination
    destPtr = cupHash[destVal]
    pickTail.next = destPtr.next
    destPtr.next = pickHead

    currPtr = currPtr.next

finalPtr = cupHash[1]
finalStr = ""
while finalPtr.next.val != 1:
    finalPtr = finalPtr.next
    finalStr += str(finalPtr.val)

print("done")
val1 = cupHash[1].next.val
val2 = cupHash[1].next.next.val

print(f'Final Val = {val1*val2}')

