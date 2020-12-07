#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

rules = {}
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.match('(.*) bags contain (.*)\.', line)
    container = m.group(1)
    contentsArray = m.group(2).split(', ')
    rules[container] = []
    if contentsArray[0] == 'no other bags':
        rules[container].append( ('None', 0) )
    else:
        for c in contentsArray:
            m = re.match('(\d+) (.*) bag', c)
            rules[container].append( (m.group(2), int(m.group(1))) )

inputFile.close()

for k in rules.keys():
    dbgPrint(k)
    for r in rules[k]:
        dbgPrint(f'  {r}')

print("------------------")
print("---- PART 1 ------")
print("------------------")

bagsToCheck = ['shiny gold']
bagsCanHold = {}

while len(bagsToCheck) > 0:
    bagToCheck = bagsToCheck.pop(0);
    for possibleBag in rules.keys():
        for content in rules[possibleBag]:
            if content[0] == bagToCheck:
                bagsCanHold[possibleBag] = True
                bagsToCheck.append(possibleBag)

print(f'Number of Color Bags = {len(bagsCanHold)}')

print("------------------")
print("---- PART 2 ------")
print("------------------")


bagsToCheck = ['shiny gold']
bagsHeld = -1 # start at -1 to account for shiny gold
while len(bagsToCheck) > 0:
    bagToCheck = bagsToCheck.pop(0);
    bagsHeld += 1
    for bag in rules[bagToCheck]:
        for i in range(0,bag[1]):
            bagsToCheck.append(bag[0])

print(f'Num Bags Held = {bagsHeld}')
