#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

ingredientSets = []
allergenSets = {}
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.match('^(.*) \(contains (.*)\)', line)
    for a in m.group(2).split(', '):
        if not a in allergenSets:
            allergenSets[a] = [m.group(1).split()]
        else:
            allergenSets[a].append(m.group(1).split())
    ingredientSets.append(m.group(1).split())

for a in allergenSets.keys():
    print(allergenSets[a])

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

# Uniquify
for a in allergenSets.keys():
    removalList = []
    for s1 in allergenSets[a]:
        for i in s1:
            for s2 in allergenSets[a]:
                if not i in s2: removalList.append(i)
    for r in removalList:
        for s in allergenSets[a]:
            if r in s:
                s.remove(r)

for a in allergenSets.keys():
    allergenSets[a] = allergenSets[a][0]
    print(allergenSets[a])

allSetsLen1 = False
knownIngreds = [] 
while not allSetsLen1:
    for a in allergenSets.keys():
        if len(allergenSets[a]) == 1: 
            if allergenSets[a][0] not in knownIngreds:
                knownIngreds.append(allergenSets[a][0])

    allSetsLen1 = True
    for a in allergenSets.keys():
        if len(allergenSets[a]) > 1: 
            allSetsLen1 = False
            for i in knownIngreds:
                if i in allergenSets[a]:
                    allergenSets[a].remove(i)

    print(knownIngreds)

for i in ingredientSets:
    for k in knownIngreds:
        if k in i: i.remove(k)

ingredSum = 0
for i in ingredientSets:
    ingredSum += len(i)

print(f"ingredient sum = {ingredSum}")

print("------------------")
print("---- PART 2 ------")
print("------------------")

allergens = sorted(allergenSets.keys())
print(allergens)
canonical = []
for a in allergens:
    canonical.append(allergenSets[a][0])

print(f'canonical = {",".join(canonical)}')

