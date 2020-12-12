#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

directions = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.match('^([NSEWLRF])(\d+)$', line)
    directions.append( (m.group(1), int(m.group(2))))
inputFile.close()

for d in directions:
    dbgPrint(d)

print("------------------")
print("---- PART 1 ------")
print("------------------")

heading = 0  # 0 = E; 90 = N
location = [0,0]  # y, x
for d in directions:
    dbgPrint(f"At {location} heading = {heading}; action = {d};   ", end = '')
    action = d[0]
    value  = d[1]
    if action == 'N':  location[0] -= value
    if action == 'S':  location[0] += value
    if action == 'E':  location[1] += value
    if action == 'W':  location[1] -= value

    if action == 'L': heading = (heading + value) % 360
    if action == 'R': heading = (heading - value) % 360

    if action == 'F' and heading ==   0: location[1] += value
    if action == 'F' and heading ==  90: location[0] -= value
    if action == 'F' and heading == 180: location[1] -= value
    if action == 'F' and heading == 270: location[0] += value

    dbgPrint(f"new location = {location}; new heading = {heading}")

print(f'distance from start = {abs(location[0]) + abs(location[1])}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
wpRelativeLoc = [-1,10]  # y, x
shipLocation  = [0,0]  # y, x
for d in directions:
    dbgPrint(f"Ship = {shipLocation} WP loc = {wpRelativeLoc}; action = {d};   ")
    action = d[0]
    value  = d[1]
    if action == 'N':  wpRelativeLoc[0] -= value
    if action == 'S':  wpRelativeLoc[0] += value
    if action == 'E':  wpRelativeLoc[1] += value
    if action == 'W':  wpRelativeLoc[1] -= value

    wpLocPrior = [0,0]
    wpLocPrior[0] = wpRelativeLoc[0]
    wpLocPrior[1] = wpRelativeLoc[1]
    if action == 'L' and value ==   0: 
        wpRelativeLoc[0] = wpLocPrior[0]
        wpRelativeLoc[1] = wpLocPrior[1]
    if action == 'L' and value ==  90:
        wpRelativeLoc[0] = -1*wpLocPrior[1]
        wpRelativeLoc[1] =    wpLocPrior[0]
    if action == 'L' and value == 180: 
        wpRelativeLoc[0] = -1*wpLocPrior[0] 
        wpRelativeLoc[1] = -1*wpLocPrior[1] 
    if action == 'L' and value == 270:
        wpRelativeLoc[0] =    wpLocPrior[1]
        wpRelativeLoc[1] = -1*wpLocPrior[0]

    if action == 'R' and value ==   0: 
        wpRelativeLoc[0] = wpLocPrior[0]
        wpRelativeLoc[1] = wpLocPrior[1]
    if action == 'R' and value ==  90:
        wpRelativeLoc[0] =    wpLocPrior[1]
        wpRelativeLoc[1] = -1*wpLocPrior[0]
    if action == 'R' and value == 180: 
        wpRelativeLoc[0] = -1*wpLocPrior[0] 
        wpRelativeLoc[1] = -1*wpLocPrior[1] 
    if action == 'R' and value == 270:
        wpRelativeLoc[0] = -1*wpLocPrior[1]
        wpRelativeLoc[1] =    wpLocPrior[0]

    if action == 'F': 
        shipLocation[1] += value * wpRelativeLoc[1]
        shipLocation[0] += value * wpRelativeLoc[0]

dbgPrint(f"Ship = {shipLocation} WP loc = {wpRelativeLoc}")

print(f'distance from start = {abs(shipLocation[0]) + abs(shipLocation[1])}')


