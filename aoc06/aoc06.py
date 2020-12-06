#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")

groups = []
newGroup = True
group = []

for line in inputFile.readlines():
    # check if blank line
    if line == "\n":
        groups.append(group)
        group = []
        continue

    group.append(list(line.strip()))

# no new line at end of file, append last entry
groups.append(group)

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

countSum = 0
for group in groups:
    answers = {}
    for person in group:
        for answer in person:
            answers[answer] = 1
    countSum += len(answers.keys())

print(f"Total Count = {countSum}")

print("------------------")
print("---- PART 2 ------")
print("------------------")

countSum = 0
for group in groups:
    answers = {}
    for person in group:
        for answer in person:
            if answer not in answers: answers[answer] = 1
            else: answers[answer] += 1
    for key in answers.keys():
        if answers[key] == len(group):
            countSum += 1

print(f"Total Count = {countSum}")


