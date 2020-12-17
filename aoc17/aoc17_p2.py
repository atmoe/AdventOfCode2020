#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

def printGrid(g):
    for w in range(len(g)):
        for z in range(len(g[0])):
            print(f'z={z} w={w}')
            for y in range(len(g[0][0])):
                print("".join(g[w][z][y]))
            print()

def increaseWidth(g, w, h, d, p):
    for a in range(p):
        for z in range(d):
            for y in range(h):
                g[a][z][y].append('.')
                g[a][z][y].insert(0, '.')

def increaseHeight(g, w, h, d, p):
    for a in range(p):
        for z in range(d):
            g[a][z].append(['.']*w)
            g[a][z].insert(0, ['.']*w)

def increaseDepth(g, w, h, d, p):
    newSlice = []
    for y in range(h):
        newSlice.append(['.']*w)

    for a in range(p):
        g[a].append(copy.deepcopy(newSlice))
        g[a].insert(0, copy.deepcopy(newSlice))

def increaseP(g, w, h, d, p):
    newSlice = []
    for z in range(d):
        newSlice.append([])
        for y in range(h):
            newSlice[z].append(['.']*w)

    g.append(copy.deepcopy(newSlice))
    g.insert(0, copy.deepcopy(newSlice))

def getCount(g, x, y, z, a, w, h, d, p):
    count = 0
    for a_off in [-1, 0, 1]:
        for z_off in [-1, 0, 1]:
            for y_off in [-1, 0, 1]:
                for x_off in [-1, 0, 1]:
                    if x_off==0 and y_off==0 and z_off==0 and a_off==0: continue
                    if (a+a_off) < 0 or (a+a_off) >= p: continue
                    if (z+z_off) < 0 or (z+z_off) >= d: continue
                    if (y+y_off) < 0 or (y+y_off) >= h: continue
                    if (x+x_off) < 0 or (x+x_off) >= w: continue

                    if g[a+a_off][z+z_off][y+y_off][x+x_off] == '#':
                        count+=1
    return count

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

grid = [[[]]]
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    grid[0][0].append(list(line.strip()))

inputFile.close()

print("--- Initial Grid ---")
printGrid(grid)

print("------------------")
print("---- PART 1 ------")
print("------------------")

numIterations = 6
gW = len(grid[0][0][0])
gH = len(grid[0][0])
gD = len(grid[0])
gP = len(grid)

# expand inactive around grid
increaseWidth(grid, gW, gH, gD, gP)
gW+=2
increaseHeight(grid, gW, gH, gD, gP)
gH+=2
increaseDepth(grid, gW, gH, gD, gP)
gD+=2
increaseP(grid, gW, gH, gD, gP)
gP+=2

print("--- Padded Grid ---")
printGrid(grid)

nextGrid = copy.deepcopy(grid)
for i in range(numIterations):
    print(f"--- Cycle {i+1} ---")
    expandW=False
    expandH=False
    expandD=False
    expandP=False
    for a in range(gP):
        for z in range(gD):
            for y in range(gH):
                for x in range(gW):
                    count = getCount(grid, x, y, z, a, gW, gH, gD, gP)
                    if grid[a][z][y][x] == '.' and count == 3:
                        nextGrid[a][z][y][x] = '#'
                    elif grid[a][z][y][x] == '#' and (count == 2 or count == 3):
                        nextGrid[a][z][y][x] = '#'
                    else:
                        nextGrid[a][z][y][x] = '.'

                    if nextGrid[a][z][y][x] == '#':
                        if a==0 or a==gP-1: expandP = True
                        if z==0 or z==gD-1: expandD = True
                        if y==0 or y==gH-1: expandH = True
                        if x==0 or x==gW-1: expandW = True


    if expandW:
        print("expanding W")
        increaseWidth(nextGrid, gW, gH, gD, gP)
        gW+=2
    if expandH:
        print("expanding H")
        increaseHeight(nextGrid, gW, gH, gD, gP)
        gH+=2
    if expandD:
        print("expanding D")
        increaseDepth(nextGrid, gW, gH, gD, gP)
        gD+=2
    if expandP:
        print("expanding P")
        increaseP(nextGrid, gW, gH, gD, gP)
        gP+=2

    printGrid(nextGrid)
    grid = copy.deepcopy(nextGrid)

totalActive = 0
for a in range(gP):
    for z in range(gD):
        for y in range(gH):
            for x in range(gW):
                if grid[a][z][y][x] == '#':
                    totalActive+=1

print(f'Total Active = {totalActive}')



print("------------------")
print("---- PART 2 ------")
print("------------------")

