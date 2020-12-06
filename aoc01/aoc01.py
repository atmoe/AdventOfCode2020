#!/usr/bin/python

import sys

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

entries = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    entries.append(int(line))

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

entryFound = False
for e1 in entries:
    for e2 in entries:
        if(e1 + e2 == 2020):
            print(f'{e1*e2}')
            entryFound=True
            break
    if entryFound: break

print("------------------")
print("---- PART 2 ------")
print("------------------")
entryFound = False
for e1 in entries:
    for e2 in entries:
        for e3 in entries:
           if(e1 + e2 + e3 == 2020):
                print(f'{e1*e2*e3}')
                entryFound=True
                break
        if entryFound: break
    if entryFound: break
