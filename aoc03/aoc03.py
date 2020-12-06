#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

grid = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    grid.append(list(line.strip()))
inputFile.close()
gridWidth  = len(grid[0])
gridHeight = len(grid)

print(f'WxH = {gridWidth}x{gridHeight}')
for l in grid:
    print("".join(l))

print("------------------")
print("---- PART 1 ------")
print("------------------")

xPos = 0
yPos = 0
numTrees = 0
while yPos < gridHeight:
    if(grid[yPos][xPos] == '#'):
        numTrees += 1

    xPos = (xPos + 3) % gridWidth
    yPos += 1

print(f'Num Trees = {numTrees}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

product = 1
for s in slopes:
    xPos = 0
    yPos = 0
    numTrees = 0
    while yPos < gridHeight:
        if(grid[yPos][xPos] == '#'):
            numTrees += 1

        xPos = (xPos + s[0]) % gridWidth
        yPos += s[1] 

    product *= numTrees

print(f'Num Trees Product = {product}')


