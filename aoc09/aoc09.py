#!/usr/bin/python

import sys
import re

debug = True
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

numbers = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    numbers.append(int(line))

inputFile.close()

preambleLen = 25 # test is 5, official input is 25
print("------------------")
print("---- PART 1 ------")
print("------------------")

step2Target = 0
for i in range(preambleLen, len(numbers)):
    localGroup = numbers[i-preambleLen:i]
    targetNum = numbers[i]
    targetFound=False
    for idx,n1 in enumerate(localGroup):
        for n2 in localGroup[idx+1:preambleLen]:
            if n1+n2 == targetNum:
                targetFound=True
                break
        if targetFound: break

    if not targetFound:
        step2Target = targetNum
        print(f"Number not sum of preamble = {targetNum}")

print("------------------")
print("---- PART 2 ------")
print("------------------")

for i in range(0, len(numbers)):
    currentSum = 0
    numNumbers = 0
    currSumIdx = i
    while currentSum < step2Target:
        currentSum += numbers[currSumIdx]
        currSumIdx += 1

    if currentSum == step2Target:
        minNum = min(numbers[i:currSumIdx])
        maxNum = max(numbers[i:currSumIdx])
        print(f"Encryption Weakness = {minNum + maxNum}")
        break





