#!/usr/bin/python

import sys
import re
import copy
import numpy as np

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

def print3DGrid(g):
    if not debug: return
    for z in range(len(g)):
        for y in range(len(g[0])):
            print("".join(g[z][y]))
        print()

def print4DGrid(g):
    if not debug: return
    for w in range(len(g)):
        for z in range(len(g[0])):
            print(f'z={z} w={w}')
            for y in range(len(g[0][0])):
                print("".join(g[w][z][y]))
            print()

def get3DCount(g, x, y, z, dims):
    count = 0
    for z_off in [-1, 0, 1]:
        for y_off in [-1, 0, 1]:
            for x_off in [-1, 0, 1]:
                if x_off==0 and y_off==0 and z_off==0: continue
                if (z+z_off) < 0 or (z+z_off) >= dims[-3]: continue
                if (y+y_off) < 0 or (y+y_off) >= dims[-2]: continue
                if (x+x_off) < 0 or (x+x_off) >= dims[-1]: continue

                if g[z+z_off][y+y_off][x+x_off] == '#':
                    count+=1
    return count

def get4DCount(g, x, y, z, w, dims):
    count = 0
    for w_off in [-1, 0, 1]:
        for z_off in [-1, 0, 1]:
            for y_off in [-1, 0, 1]:
                for x_off in [-1, 0, 1]:
                    if x_off==0 and y_off==0 and z_off==0 and w_off==0: continue
                    if (w+w_off) < 0 or (w+w_off) >= dims[-4]: continue
                    if (z+z_off) < 0 or (z+z_off) >= dims[-3]: continue
                    if (y+y_off) < 0 or (y+y_off) >= dims[-2]: continue
                    if (x+x_off) < 0 or (x+x_off) >= dims[-1]: continue

                    if g[w+w_off][z+z_off][y+y_off][x+x_off] == '#':
                        count+=1
    return count

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"


def increaseDim(g, d, axis, direction):
    xS = 0
    xE = d[-1]
    yS = 0
    yE = d[-2]
    zS = 0
    zE = d[-3]
    if len(d) == 4:
        wS = 0
        wE = d[-4]
    if axis == 'width':
        d[-1] += 1
        if direction == -1:
            xS += 1
            xE += 1
    if axis == 'height':
        d[-2] += 1
        if direction == -1:
            yS += 1
            yE += 1
    if axis == 'depth':
        d[-3] += 1
        if direction == -1:
            zS += 1
            zE += 1
    if axis == 'fourth':
        d[-4] += 1
        if direction == -1:
            wS += 1
            wE += 1
    newGrid = np.chararray(shape=d, unicode=True)
    newGrid.fill('.')

    if len(d) == 3:
        newGrid[zS:zE,yS:yE,xS:xE] = g
    if len(d) == 4:
        newGrid[wS:wE,zS:zE,yS:yE,xS:xE] = g

    return newGrid

grid2D = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    grid2D.append(list(line.strip()))
inputFile.close()


print("------------------")
print("---- PART 1 ------")
print("------------------")

dims = [1, len(grid2D), len(grid2D[0])] # Depth, Height, Width
grid = np.chararray(shape=dims, unicode=True)
grid.fill('.')
for y in range(len(grid2D)):
    for x in range(len(grid2D[0])):
            grid[0][y][x] = grid2D[y][x]

dbgPrint("--- Initial Grid ---")
print3DGrid(grid)

dbgPrint("--- Padded Grid ---")
grid = increaseDim(grid, dims, 'width',   1)
grid = increaseDim(grid, dims, 'width',  -1)
grid = increaseDim(grid, dims, 'height',  1)
grid = increaseDim(grid, dims, 'height', -1)
grid = increaseDim(grid, dims, 'depth',   1)
grid = increaseDim(grid, dims, 'depth',  -1)
print3DGrid(grid)

numIterations = 6

nextGrid = copy.deepcopy(grid)
for i in range(numIterations):
    dbgPrint(f"--- Cycle {i+1} ---")
    expandW_pos=False
    expandW_neg=False
    expandH_pos=False
    expandH_neg=False
    expandD_pos=False
    expandD_neg=False
    for z in range(dims[0]):
        for y in range(dims[1]):
            for x in range(dims[2]):
                count = get3DCount(grid, x, y, z, dims)
                if grid[z][y][x] == '.' and count == 3:
                    nextGrid[z][y][x] = '#'
                elif grid[z][y][x] == '#' and (count == 2 or count == 3):
                    nextGrid[z][y][x] = '#'
                else:
                    nextGrid[z][y][x] = '.'

                if nextGrid[z][y][x] == '#':
                    if z==0:          expandD_neg = True
                    if y==0:          expandH_neg = True
                    if x==0:          expandW_neg = True
                    if z==dims[-3]-1: expandD_pos = True
                    if y==dims[-2]-1: expandH_pos = True
                    if x==dims[-1]-1: expandW_pos = True

    if expandW_pos: nextGrid = increaseDim(nextGrid, dims, 'width',   1)
    if expandW_neg: nextGrid = increaseDim(nextGrid, dims, 'width',  -1)
    if expandH_pos: nextGrid = increaseDim(nextGrid, dims, 'height',  1)
    if expandH_neg: nextGrid = increaseDim(nextGrid, dims, 'height', -1)
    if expandD_pos: nextGrid = increaseDim(nextGrid, dims, 'depth',   1)
    if expandD_neg: nextGrid = increaseDim(nextGrid, dims, 'depth',  -1)

    print3DGrid(nextGrid)
    grid = copy.deepcopy(nextGrid)

totalActive = 0
for z in range(dims[-3]):
    for y in range(dims[-2]):
        for x in range(dims[-1]):
            if grid[z][y][x] == '#':
                totalActive+=1

print(f'Total Active = {totalActive}')


print("------------------")
print("---- PART 2 ------")
print("------------------")
dims = [1, 1, len(grid2D), len(grid2D[0])] # Depth, Height, Width
grid = np.chararray(shape=dims, unicode=True)
grid.fill('.')
for y in range(len(grid2D)):
    for x in range(len(grid2D[0])):
        grid[0][0][y][x] = grid2D[y][x]

dbgPrint("--- Initial Grid ---")
print4DGrid(grid)

dbgPrint("--- Padded Grid ---")
grid = increaseDim(grid, dims, 'width',   1)
grid = increaseDim(grid, dims, 'width',  -1)
grid = increaseDim(grid, dims, 'height',  1)
grid = increaseDim(grid, dims, 'height', -1)
grid = increaseDim(grid, dims, 'depth',   1)
grid = increaseDim(grid, dims, 'depth',  -1)
grid = increaseDim(grid, dims, 'fourth',  1)
grid = increaseDim(grid, dims, 'fourth', -1)
print4DGrid(grid)

numIterations = 6

nextGrid = copy.deepcopy(grid)
for i in range(numIterations):
    dbgPrint(f"--- Cycle {i+1} ---")
    expandW_pos=False
    expandW_neg=False
    expandH_pos=False
    expandH_neg=False
    expandD_pos=False
    expandD_neg=False
    expand4_pos=False
    expand4_neg=False
    for w in range(dims[-4]):
        for z in range(dims[-3]):
            for y in range(dims[-2]):
                for x in range(dims[-1]):
                    count = get4DCount(grid, x, y, z, w, dims)
                    if grid[w][z][y][x] == '.' and count == 3:
                        nextGrid[w][z][y][x] = '#'
                    elif grid[w][z][y][x] == '#' and (count == 2 or count == 3):
                        nextGrid[w][z][y][x] = '#'
                    else:
                        nextGrid[w][z][y][x] = '.'

                    if nextGrid[w][z][y][x] == '#':
                        if w==0:          expand4_neg = True
                        if z==0:          expandD_neg = True
                        if y==0:          expandH_neg = True
                        if x==0:          expandW_neg = True
                        if z==dims[-4]-1: expand4_pos = True
                        if z==dims[-3]-1: expandD_pos = True
                        if y==dims[-2]-1: expandH_pos = True
                        if x==dims[-1]-1: expandW_pos = True

    if expandW_pos: nextGrid = increaseDim(nextGrid, dims, 'width',   1)
    if expandW_neg: nextGrid = increaseDim(nextGrid, dims, 'width',  -1)
    if expandH_pos: nextGrid = increaseDim(nextGrid, dims, 'height',  1)
    if expandH_neg: nextGrid = increaseDim(nextGrid, dims, 'height', -1)
    if expandD_pos: nextGrid = increaseDim(nextGrid, dims, 'depth',   1)
    if expandD_neg: nextGrid = increaseDim(nextGrid, dims, 'depth',  -1)
    if expand4_pos: nextGrid = increaseDim(nextGrid, dims, 'fourth',  1)
    if expand4_neg: nextGrid = increaseDim(nextGrid, dims, 'fourth', -1)

    print4DGrid(nextGrid)
    grid = copy.deepcopy(nextGrid)

totalActive = 0
for w in range(dims[-4]):
    for z in range(dims[-3]):
        for y in range(dims[-2]):
            for x in range(dims[-1]):
                if grid[w][z][y][x] == '#':
                    totalActive+=1

print(f'Total Active = {totalActive}')


