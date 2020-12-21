#!/usr/bin/python

import sys
import re
import copy

debug = True
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

class Tile:
    def __init__(self, num, array):
        self.num = num
        self.size = len(array)
        self.array = copy.deepcopy(array)
        self.numAdj = 0
        self.adjMsk = [-1, -1, -1, -1] # [T, R, B, L]

        self.t = "".join(self.array[0])
        self.b = "".join(self.array[-1])
        right = []
        left  = []
        for row in self.array:
            right.append(row[-1])
            left.append(row[0])
        self.r = "".join(right)
        self.l = "".join(left)

    def matchEdge(self, edge, num):
        self.numAdj += 1
        if edge == 't': idx = 0
        if edge == 'r': idx = 1
        if edge == 'b': idx = 2
        if edge == 'l': idx = 3
        self.adjMsk[idx] = num

    # Rotate Clockwise
    def rotate90(self):
        self.adjMsk = [self.adjMsk[-1]] + self.adjMsk[0:3]
        newArray = [['.' for x in range(self.size)] for y in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                newArray[x][self.size - y - 1] = self.array[y][x]
        self.array = newArray

    # Flip over horizontal axis
    def flipY(self):
        self.adjMsk = [self.adjMsk[2], self.adjMsk[1], self.adjMsk[0], self.adjMsk[3]]
        newArray = [['.' for x in range(self.size)] for y in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                newArray[self.size - y - 1][x] = self.array[y][x]
        self.array = newArray

    # Flip over vertical axis
    def flipX(self):
        self.adjMsk = [self.adjMsk[0], self.adjMsk[3], self.adjMsk[2], self.adjMsk[1]]
        newArray = [['.' for x in range(self.size)] for y in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                newArray[y][self.size - x - 1] = self.array[y][x]
        self.array = newArray

    def getTileArr(self):
        arr = []
        for row in self.array[1:-1]:
            arr.append(row[1:-1])
        return arr

    def display(self):
        for r in self.array:
            print("".join(r))
        print()
        print(f"msk = {self.adjMsk}")

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

tiles = {}

curTileNum = 0
curTile = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if line == '\n': 
        newTile = Tile(curTileNum, curTile)
        tiles[curTileNum] = newTile
        print(curTileNum)
        continue

    m = re.match('^Tile (\d+):', line)
    if m: 
        curTileNum = int(m.group(1))
        curTile = []
        continue

    curTile.append(list(line.strip()))

inputFile.close()

for t in tiles.keys():
    print("------------")
    tiles[t].display()

print("------------------")
print("---- PART 1 ------")
print("------------------")

numEdgeTiles = 0

cornerMult = 1
cornerTiles = []
edgeTiles   = []
middleTiles = []
for t1num in tiles.keys():
    tile1 = tiles[t1num]

    matches = 0
    mask = 0
    for t2num in tiles.keys():
        if t1num == t2num: continue

        tile2 = tiles[t2num]

        if tile1.l == tile2.t[::-1]: tile1.matchEdge('l', t2num)
        if tile1.l == tile2.l[::-1]: tile1.matchEdge('l', t2num)  
        if tile1.l == tile2.r[::-1]: tile1.matchEdge('l', t2num)  
        if tile1.l == tile2.b[::-1]: tile1.matchEdge('l', t2num)  
        if tile1.r == tile2.t[::-1]: tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.l[::-1]: tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.r[::-1]: tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.b[::-1]: tile1.matchEdge('r', t2num)  
        if tile1.t == tile2.t[::-1]: tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.l[::-1]: tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.r[::-1]: tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.b[::-1]: tile1.matchEdge('t', t2num)  
        if tile1.b == tile2.t[::-1]: tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.l[::-1]: tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.r[::-1]: tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.b[::-1]: tile1.matchEdge('b', t2num)  
        if tile1.l == tile2.t:       tile1.matchEdge('l', t2num)  
        if tile1.l == tile2.l:       tile1.matchEdge('l', t2num)  
        if tile1.l == tile2.r:       tile1.matchEdge('l', t2num)  
        if tile1.l == tile2.b:       tile1.matchEdge('l', t2num)  
        if tile1.r == tile2.t:       tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.l:       tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.r:       tile1.matchEdge('r', t2num)  
        if tile1.r == tile2.b:       tile1.matchEdge('r', t2num)  
        if tile1.t == tile2.t:       tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.l:       tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.r:       tile1.matchEdge('t', t2num)  
        if tile1.t == tile2.b:       tile1.matchEdge('t', t2num)  
        if tile1.b == tile2.t:       tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.l:       tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.r:       tile1.matchEdge('b', t2num)  
        if tile1.b == tile2.b:       tile1.matchEdge('b', t2num)  

    dbgPrint(f'tile {t1num} has {matches} matches')
    if tile1.numAdj == 2: cornerMult *= t1num


    if tile1.numAdj == 2: cornerTiles.append(t1num)
    if tile1.numAdj == 3: edgeTiles.append(t1num)
    if tile1.numAdj == 4: middleTiles.append(t1num)


print(f'Multiplication = {cornerMult}')


print("------------------")
print("---- PART 2 ------")
print("------------------")
def isMonster(grid, x_o, y_o):
    if grid[y_o + 1][x_o + 0] != '#': return False
    if grid[y_o + 2][x_o + 1] != '#': return False
    if grid[y_o + 2][x_o + 4] != '#': return False
    if grid[y_o + 1][x_o + 5] != '#': return False
    if grid[y_o + 1][x_o + 6] != '#': return False
    if grid[y_o + 2][x_o + 7] != '#': return False
    if grid[y_o + 2][x_o +10] != '#': return False
    if grid[y_o + 1][x_o +11] != '#': return False
    if grid[y_o + 1][x_o +12] != '#': return False
    if grid[y_o + 2][x_o +13] != '#': return False
    if grid[y_o + 2][x_o +16] != '#': return False
    if grid[y_o + 1][x_o +17] != '#': return False
    if grid[y_o + 1][x_o +18] != '#': return False
    if grid[y_o + 0][x_o +18] != '#': return False
    if grid[y_o + 1][x_o +19] != '#': return False

    grid[y_o + 1][x_o + 0] = 'O'
    grid[y_o + 2][x_o + 1] = 'O'
    grid[y_o + 2][x_o + 4] = 'O'
    grid[y_o + 1][x_o + 5] = 'O'
    grid[y_o + 1][x_o + 6] = 'O'
    grid[y_o + 2][x_o + 7] = 'O'
    grid[y_o + 2][x_o +10] = 'O'
    grid[y_o + 1][x_o +11] = 'O'
    grid[y_o + 1][x_o +12] = 'O'
    grid[y_o + 2][x_o +13] = 'O'
    grid[y_o + 2][x_o +16] = 'O'
    grid[y_o + 1][x_o +17] = 'O'
    grid[y_o + 1][x_o +18] = 'O'
    grid[y_o + 0][x_o +18] = 'O'
    grid[y_o + 1][x_o +19] = 'O'
    return True

tilesPerEdge = int(len(edgeTiles)/4) + 2
print(f'tilesPerEdge = {tilesPerEdge}')

tileGrid = [[-1 for x in range(tilesPerEdge)] for y in range(tilesPerEdge)]

for y in range(tilesPerEdge):
    for x in range(tilesPerEdge):
        # TL
        if (y==0 and x==0):
            tile = tiles[cornerTiles[0]]
            tile.flipY() # to match official example
            tileGrid[y][x] = tile.num
            #cornerTiles.pop()
            while not (tile.adjMsk[0] == -1 and tile.adjMsk[3] == -1): tile.rotate90()
            #tile.display()

        # Top Edge
        elif y==0:
            thisTileID = tiles[tileGrid[0][x-1]].adjMsk[1]
            leftTileID = tiles[tileGrid[0][x-1]].num

            tile = tiles[thisTileID]
            tileGrid[y][x] = tile.num

            while not (tile.adjMsk[3] == leftTileID): tile.rotate90()
            if tile.adjMsk[0] != -1: tile.flipY()
            #tile.display()

        # Left Edge
        elif x==0:
            thisTileID = tiles[tileGrid[y-1][0]].adjMsk[2]
            topTileID  = tiles[tileGrid[y-1][0]].num

            tile = tiles[thisTileID]
            tileGrid[y][x] = tile.num

            while not (tile.adjMsk[0] == topTileID): tile.rotate90()
            if tile.adjMsk[3] != -1: tile.flipX()

        # Everything else looks like "middle"
        else:
            thisTileID = tiles[tileGrid[y][x-1]].adjMsk[1]
            leftTileID = tiles[tileGrid[y][x-1]].num
            topTileID  = tiles[tileGrid[y-1][0]].num

            tile = tiles[thisTileID]
            tileGrid[y][x] = tile.num

            while not (tile.adjMsk[3] == leftTileID): tile.rotate90()
            if tile.adjMsk[0] != topTileID: tile.flipY()
            #tile.display()

        print(tileGrid[y][x], end=' ')

    print()

finalGrid = []
numHashes = 0
for y in range(tilesPerEdge):
    for x in range(tilesPerEdge):
        arr = tiles[tileGrid[y][x]].getTileArr()
        for idx,a in enumerate(arr):
            if x == 0:
                finalGrid.append(a)
            else:
                finalGrid[y*8+idx] += a

fW = len(finalGrid[0])
fH = len(finalGrid)
for r in finalGrid:
    print("".join(r))

finalGrid90   = [['.' for x in range(fW)] for y in range(fH)]
finalGrid180  = [['.' for x in range(fW)] for y in range(fH)]
finalGrid270  = [['.' for x in range(fW)] for y in range(fH)]
finalGridF    = [['.' for x in range(fW)] for y in range(fH)]
finalGrid90F  = [['.' for x in range(fW)] for y in range(fH)]
finalGrid180F = [['.' for x in range(fW)] for y in range(fH)]
finalGrid270F = [['.' for x in range(fW)] for y in range(fH)]
for y in range(fH):
    for x in range(fW):
        if finalGrid[y][x] == '#': numHashes += 1
        finalGrid90[x][fH - y - 1] = finalGrid[y][x]
for y in range(fH):
    for x in range(fW):
        finalGrid180[x][fH - y - 1] = finalGrid90[y][x]
for y in range(fH):
    for x in range(fW):
        finalGrid270[x][fH - y - 1] = finalGrid180[y][x]
for y in range(fH):
    for x in range(fW):
        finalGridF[fH - y - 1][x]    = finalGrid[y][x]
        finalGrid90F[fH - y - 1][x]  = finalGrid90[y][x]
        finalGrid180F[fH - y - 1][x] = finalGrid180[y][x]
        finalGrid270F[fH - y - 1][x] = finalGrid270[y][x]

numMonster0   = 0
numMonster90  = 0
numMonster180 = 0
numMonster270 = 0
numMonster0F   = 0
numMonster90F  = 0
numMonster180F = 0
numMonster270F = 0
for y in range(fH - 2):
    for x in range(fW - 19):
        if isMonster(finalGrid,     x, y): numMonster0+=1
        if isMonster(finalGrid90,   x, y): numMonster90+=1
        if isMonster(finalGrid180,  x, y): numMonster180+=1
        if isMonster(finalGrid270,  x, y): numMonster270+=1
        if isMonster(finalGridF,    x, y): numMonster0F+=1
        if isMonster(finalGrid90F,  x, y): numMonster90F+=1
        if isMonster(finalGrid180F, x, y): numMonster180F+=1
        if isMonster(finalGrid270F, x, y): numMonster270F+=1

print(f'Num Hashes      = {numHashes}')
print(f'Num Monster   0 = {numMonster0}')
print(f'Num Monster  90 = {numMonster90}')
print(f'Num Monster 180 = {numMonster180}')
print(f'Num Monster 270 = {numMonster270}')
print(f'Num Monster   0F = {numMonster0F}')
print(f'Num Monster  90F = {numMonster90F}')
print(f'Num Monster 180F = {numMonster180F}')
print(f'Num Monster 270F = {numMonster270F}')


for r in finalGrid270F:
    print("".join(r))
