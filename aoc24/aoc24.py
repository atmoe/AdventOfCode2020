#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dirList = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    steps = []
    get2ndLetter = False
    lastLetter = 'x'
    for c in list(line.strip()):
        if get2ndLetter:
            steps.append(lastLetter+c) 
            get2ndLetter=False
        elif c == 'e' or c == 'w':
            steps.append(c)
        else:
            get2ndLetter=True
            lastLetter = c

    dirList.append(steps)

inputFile.close()

for d in dirList:
    dbgPrint(d)

print("------------------")
print("---- PART 1 ------")
print("------------------")

tiles = {}
for d in dirList:
    hexRow = 0.0
    hexCol = 0.0
    for s in d:
        if s == 'w':
            hexCol -= 1.0
        elif s == 'e':
            hexCol += 1.0
        elif s == 'sw':
            hexRow+=1.0
            hexCol-=0.5
        elif s == 'se':
            hexRow+=1.0
            hexCol+=0.5
        elif s == 'nw':
            hexRow-=1.0
            hexCol-=0.5
        elif s == 'ne':
            hexRow-=1.0
            hexCol+=0.5

    dbgPrint(f'{hexRow} {hexCol}')
    hashKey =(hexRow, hexCol)
    if not hashKey in tiles.keys():
        tiles[hashKey] = False
    else:
        tiles[hashKey] = not tiles[hashKey]


numBlack = 0
for k in tiles.keys():
    if tiles[k] == False:
        numBlack+=1

print(f'Num Black Tiles = {numBlack}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

for day in range(100):
    # add adjacent white tiles for every black tile
    newWhite = []
    for tile in tiles.keys():
        color = tiles[tile]
        if color == False:
            adj1 = (tile[0]+0.0, tile[1]-1.0) # w
            adj2 = (tile[0]+0.0, tile[1]+1.0) # e
            adj3 = (tile[0]+1.0, tile[1]-0.5) # sw
            adj4 = (tile[0]+1.0, tile[1]+0.5) # se
            adj5 = (tile[0]-1.0, tile[1]-0.5) # nw
            adj6 = (tile[0]-1.0, tile[1]+0.5) # ne
            if not adj1 in tiles.keys(): newWhite.append(adj1)
            if not adj2 in tiles.keys(): newWhite.append(adj2)
            if not adj3 in tiles.keys(): newWhite.append(adj3)
            if not adj4 in tiles.keys(): newWhite.append(adj4)
            if not adj5 in tiles.keys(): newWhite.append(adj5)
            if not adj6 in tiles.keys(): newWhite.append(adj6)

    for n in newWhite:
        tiles[n] = True

    newTiles = {}
    for tile in tiles.keys():
        numBlack = 0
        color = tiles[tile]
        adj1 = (tile[0]+0.0, tile[1]-1.0) # w
        adj2 = (tile[0]+0.0, tile[1]+1.0) # e
        adj3 = (tile[0]+1.0, tile[1]-0.5) # sw
        adj4 = (tile[0]+1.0, tile[1]+0.5) # se
        adj5 = (tile[0]-1.0, tile[1]-0.5) # nw
        adj6 = (tile[0]-1.0, tile[1]+0.5) # ne

        if adj1 in tiles.keys() and tiles[adj1] == False: numBlack+=1
        if adj2 in tiles.keys() and tiles[adj2] == False: numBlack+=1
        if adj3 in tiles.keys() and tiles[adj3] == False: numBlack+=1
        if adj4 in tiles.keys() and tiles[adj4] == False: numBlack+=1
        if adj5 in tiles.keys() and tiles[adj5] == False: numBlack+=1
        if adj6 in tiles.keys() and tiles[adj6] == False: numBlack+=1

        if color == True and numBlack == 2:
            newTiles[tile] = False
        elif color == False and (numBlack == 0 or numBlack > 2):
            newTiles[tile] = True
        else:
            newTiles[tile] = tiles[tile]

    tiles = newTiles
    numBlack = 0
    for k in tiles.keys():
        if tiles[k] == False:
            numBlack+=1

    if day < 99:
        dbgPrint(f'Day {day+1}: {numBlack}')


print(f'Day {day+1}: {numBlack}')



