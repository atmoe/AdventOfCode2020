#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

def printGrid(g):
    for z in range(len(g)):
        for y in range(len(g[0])):
            print("".join(g[z][y]))
        print()

def increaseWidth(g, w, h, d):
    for z in range(d):
        for y in range(h):
            g[z][y].append('.')
            g[z][y].insert(0, '.')

def increaseHeight(g, w, h, d):
    for z in range(d):
        g[z].append(['.']*w)
        g[z].insert(0, ['.']*w)

def increaseDepth(g, w, h, d):
    newSlice = []
    for y in range(h):
        newSlice.append(['.']*w)

    g.append(newSlice)
    g.insert(0, copy.deepcopy(newSlice))

def getCount(g, x, y, z, w, h, d):
    count = 0
    for z_off in [-1, 0, 1]:
        for y_off in [-1, 0, 1]:
            for x_off in [-1, 0, 1]:
                if x_off==0 and y_off==0 and z_off==0: continue
                if (z+z_off) < 0 or (z+z_off) >= d: continue
                if (y+y_off) < 0 or (y+y_off) >= h: continue
                if (x+x_off) < 0 or (x+x_off) >= w: continue

                if g[z+z_off][y+y_off][x+x_off] == '#':
                    count+=1
    return count

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

grid = [[]]
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    grid[0].append(list(line.strip()))

inputFile.close()

print("--- Initial Grid ---")
printGrid(grid)

print("------------------")
print("---- PART 1 ------")
print("------------------")

numIterations = 6
gW = len(grid[0][0])
gH = len(grid[0])
gD = len(grid)

# expand inactive around grid
increaseWidth(grid, gW, gH, gD)
gW+=2
increaseHeight(grid, gW, gH, gD)
gH+=2
increaseDepth(grid, gW, gH, gD)
gD+=2

print("--- Padded Grid ---")
printGrid(grid)

nextGrid = copy.deepcopy(grid)
for i in range(numIterations):
    print(f"--- Cycle {i+1} ---")
    expandW=False
    expandH=False
    expandD=False
    for z in range(gD):
        for y in range(gH):
            for x in range(gW):
                count = getCount(grid, x, y, z, gW, gH, gD)
                if grid[z][y][x] == '.' and count == 3:
                    nextGrid[z][y][x] = '#'
                elif grid[z][y][x] == '#' and (count == 2 or count == 3):
                    nextGrid[z][y][x] = '#'
                else:
                    nextGrid[z][y][x] = '.'

                if nextGrid[z][y][x] == '#':
                    if z==0 or z==gD-1: expandD = True
                    if y==0 or y==gH-1: expandH = True
                    if x==0 or x==gW-1: expandW = True

    if expandW:
        increaseWidth(nextGrid, gW, gH, gD)
        gW+=2
    if expandH:
        increaseHeight(nextGrid, gW, gH, gD)
        gH+=2
    if expandD:
        increaseDepth(nextGrid, gW, gH, gD)
        gD+=2

    printGrid(nextGrid)
    grid = copy.deepcopy(nextGrid)

totalActive = 0
for z in range(gD):
    for y in range(gH):
        for x in range(gW):
            if grid[z][y][x] == '#':
                totalActive+=1

print(f'Total Active = {totalActive}')



print("------------------")
print("---- PART 2 ------")
print("------------------")

