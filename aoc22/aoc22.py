#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

player1 = []
player2 = []
mode = 'player1'
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if line == '\n': continue

    if re.match('^Player 1:', line):
        mode = 'player1'
        continue

    if re.match('^Player 2:', line):
        mode = 'player2'
        continue

    if mode == 'player1':
        player1.append(int(line.strip()))

    if mode == 'player2':
        player2.append(int(line.strip()))
inputFile.close()

print(player1)
print(player2)

print("------------------")
print("---- PART 1 ------")
print("------------------")

p1_player1 = copy.deepcopy(player1)
p1_player2 = copy.deepcopy(player2)
rndNum = 1
while len(p1_player1) > 0 and len(p1_player2) > 0:
    dbgPrint(f"--- Round {rndNum} --- ")
    if p1_player1[0] > p1_player2[0]:
        p1_player1.append(p1_player1[0])
        p1_player1.append(p1_player2[0])
        p1_player1 = p1_player1[1:] 
        p1_player2 = p1_player2[1:] 
    else:
        p1_player2.append(p1_player2[0])
        p1_player2.append(p1_player1[0])
        p1_player1 = p1_player1[1:] 
        p1_player2 = p1_player2[1:] 

    dbgPrint(f'p1 = {p1_player1}')
    dbgPrint(f'p2 = {p1_player2}')
    rndNum += 1

if len(p1_player1) == 0:
    winner = p1_player2
else:
    winner = p1_player1

score = 0
for idx,n in enumerate(reversed(winner)):
    score += (idx+1)*n

print(f'Score = {score}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

gameNum=1

def getScore(deck):
    s = 0
    for idx,n in enumerate(reversed(deck)): s += (idx+1)*n
    return s

def playGame(num, deck1, deck2):
    rndNum = 1
    p1 = copy.deepcopy(deck1)
    p2 = copy.deepcopy(deck2)
    p1scores = []
    p2scores = []
    while len(p1) > 0 and len(p2) > 0:
        dbgPrint(f"--- Round {rndNum} (Game {num}) --- ")
        dbgPrint(f'p1 = {p1}')
        dbgPrint(f'p2 = {p2}')
        dbgPrint(f'p1 draws = {p1[0]}')
        dbgPrint(f'p2 draws = {p2[0]}')

        # check if initial condition
        infiniteGame = False
        if rndNum > 1 and (getScore(p1) in p1scores) and (getScore(p2) in p2scores):
            infiniteGame = True

            if infiniteGame:
                dbgPrint(f'Player1 wins round {rndNum} game {num}! (inf)')
                break

        p1scores.append(getScore(p1))
        p2scores.append(getScore(p2))

        if not infiniteGame and p1[0] <= (len(p1) - 1) and p2[0] <= (len(p2) - 1):
            global gameNum
            gameNum+=1
            (w, scr) = playGame(gameNum, p1[1:p1[0]+1], p2[1:p2[0]+1])
            if w == 'player1':
                p1.append(p1[0])
                p1.append(p2[0])
                dbgPrint(f'Player1 wins round {rndNum} game {num}! (rec)')
            else:
                p2.append(p2[0])
                p2.append(p1[0])
                dbgPrint(f'Player2 wins round {rndNum} game {num}! (rec)')
            p1= p1[1:] 
            p2= p2[1:] 

        else:
            if p1[0] > p2[0]:
                p1.append(p1[0])
                p1.append(p2[0])
                dbgPrint(f'Player1 wins round {rndNum} game {num}! (max)')
            else:
                p2.append(p2[0])
                p2.append(p1[0])
                dbgPrint(f'Player2 wins round {rndNum} game {num}! (max)')

            p1= p1[1:] 
            p2= p2[1:] 

        rndNum += 1

    if len(p1) == 0:
        dbgPrint(p2)
        dbgPrint(f'Player2 wins game {num}!')
        dbgPrint(f'score {getScore(p2)}')
        return ('player2', getScore(p2))
    elif len(p2) == 0 or infiniteGame:
        dbgPrint(p1)
        dbgPrint(f'Player1 wins game {num}!')
        dbgPrint(f'score {getScore(p1)}')
        return ('player1', getScore(p1))


(winner, score) = playGame(gameNum, player1, player2)

print(f'Score = {score}')

