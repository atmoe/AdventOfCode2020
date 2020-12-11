#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

seatGrid = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    seatGrid.append(list(line.strip()))


inputFile.close()

def simulateGrid(grid):
    h = len(grid)
    w = len(grid[0])
    newGrid = []
    for y in range(len(grid)):
        gridRow = []
        for x in range(len(grid[y])):
            occupied = 0
            if (y != 0)   and (x != 0)   and grid[y-1][x-1] == "#": occupied += 1 # TL
            if (y != 0)   and                grid[y-1][x  ] == "#": occupied += 1 # T
            if (y != 0)   and (x != w-1) and grid[y-1][x+1] == "#": occupied += 1 # TR
            if                (x != 0  ) and grid[y  ][x-1] == "#": occupied += 1 # L
            if                (x != w-1) and grid[y  ][x+1] == "#": occupied += 1 # R
            if (y != h-1) and (x != 0  ) and grid[y+1][x-1] == "#": occupied += 1 # BL
            if (y != h-1) and                grid[y+1][x  ] == "#": occupied += 1 # B
            if (y != h-1) and (x != w-1) and grid[y+1][x+1] == "#": occupied += 1 # BR

            if grid[y][x] == '.':
                gridRow.append('.')
            elif grid[y][x] == 'L' and (occupied == 0):
                gridRow.append('#')
            elif grid[y][x] == '#' and (occupied >= 4):
                gridRow.append('L')
            else:
                gridRow.append(grid[y][x])
        newGrid.append(gridRow)
    return newGrid

# returns true if occupied
def walkGrid(grid, y0, x0, dY, dX):
    h = len(grid)
    w = len(grid[0])

    x = x0 + dX
    y = y0 + dY
    while y >= 0 and y <= h-1 and x >= 0 and x <= w-1:
        if grid[y][x] == 'L': return False
        if grid[y][x] == '#': return True

        x+=dX
        y+=dY 
    return False

def simulateGridPhase2(grid):
    h = len(grid)
    w = len(grid[0])
    newGrid = []
    for y in range(len(grid)):
        gridRow = []
        for x in range(len(grid[y])):
            occupied = 0
            if walkGrid(grid, y, x, -1, -1): occupied += 1 # TL
            if walkGrid(grid, y, x, -1,  0): occupied += 1 # T
            if walkGrid(grid, y, x, -1,  1): occupied += 1 # TR
            if walkGrid(grid, y, x,  0, -1): occupied += 1 # L
            if walkGrid(grid, y, x,  0,  1): occupied += 1 # R
            if walkGrid(grid, y, x,  1, -1): occupied += 1 # BL
            if walkGrid(grid, y, x,  1,  0): occupied += 1 # B
            if walkGrid(grid, y, x,  1,  1): occupied += 1 # BR


            if grid[y][x] == '.':
                gridRow.append('.')
            elif grid[y][x] == 'L' and (occupied == 0):
                gridRow.append('#')
            elif grid[y][x] == '#' and (occupied >= 5):
                gridRow.append('L')
            else:
                gridRow.append(grid[y][x])
        newGrid.append(gridRow)
    return newGrid

def printGrid(grid):
    if not debug: return
    print("------------------------------------")
    for g in grid:
        print("".join(g))


print("------------------")
print("---- PART 1 ------")
print("------------------")

seatsTaken = 0
converged = False
lastGrid = seatGrid
while not converged:
    printGrid(lastGrid)
    newGrid = simulateGrid(lastGrid)

    converged = True
    seatsTaken = 0
    for y in range(len(newGrid)):
        for x in range(len(newGrid[y])):
            if newGrid[y][x] == '#': seatsTaken += 1
            if(newGrid[y][x] != lastGrid[y][x]):
                converged = False
                break;
        if not converged: break;

    lastGrid = newGrid

print(f"Seats Taken = {seatsTaken}")


print("------------------")
print("---- PART 2 ------")
print("------------------")

seatsTaken = 0
converged = False
lastGrid = seatGrid
while not converged:
    printGrid(lastGrid)
    newGrid = simulateGridPhase2(lastGrid)
    
    converged = True
    seatsTaken = 0
    for y in range(len(newGrid)):
        for x in range(len(newGrid[y])):
            if newGrid[y][x] == '#': seatsTaken += 1
            if(newGrid[y][x] != lastGrid[y][x]):
                converged = False
                break;
        if not converged: break;
        
    lastGrid = newGrid
        
print(f"Seats Taken = {seatsTaken}")

