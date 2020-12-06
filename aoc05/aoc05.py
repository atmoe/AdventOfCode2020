#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")

tickets = []
for line in inputFile.readlines():
    tickets.append(list(line.strip()))
inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

# F - lower / 0
# B - upper / 1
# L - lower / 0
# R - upper / 1
seatIDs = []
for t in tickets:
    row = 0
    for i in range(7):
        row = row << 1
        if t[i] == "B": row = row | 1
    col = 0
    for i in range(7,10):
        col = col << 1
        if t[i] == "R": col = col | 1

    seatIDs.append(row*8 + col)

maxID = max(seatIDs)

print(f'highest seat ID = {maxID}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
seatIDs = []
for t in tickets:
    row = 0
    for i in range(7):
        row = row << 1
        if t[i] == "B": row = row | 1
    col = 0
    for i in range(7,10):
        col = col << 1
        if t[i] == "R": col = col | 1

    seatIDs.append(row*8 + col)

seatIDs.sort()
mySeat = 0
for idx,seat in enumerate(seatIDs):
    if idx == len(seatIDs)-1: continue

    if seat+1 != seatIDs[idx+1]:
        mySeat = seat + 1

print(f'My Seat = {mySeat}')
