#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

rules = {}
myTicket = []
tickets= []

inputMode = 'rules'
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if line == "\n":
        continue
    elif line == "your ticket:\n":
        inputMode = 'my ticket'
        continue
    elif line == "nearby tickets:\n":
        inputMode = 'tickets'
        continue

    if inputMode == 'rules':
        m = re.match('^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        if not m:
            print(f"rule doesn't match!  {line}")
            break
        name         = m.group(1)
        range1_start = int(m.group(2))
        range1_end   = int(m.group(3))
        range2_start = int(m.group(4))
        range2_end   = int(m.group(5))
        rules[name] = [[range1_start, range1_end], [range2_start, range2_end]]

    if inputMode == 'my ticket':
        myTicket = [int(i) for i in line.strip().split(',')]

    if inputMode == 'tickets':
        tickets.append([int(i) for i in line.strip().split(',')])

inputFile.close()

dbgPrint(rules)
dbgPrint(myTicket)
dbgPrint(tickets)

print("------------------")
print("---- PART 1 ------")
print("------------------")
validTickets = [] # for Part2
numInvalid = 0
errorScanningRate = 0
for t in tickets:
    ticketValid = True
    for val in t:
        valueValidForSomeRule = False
        for rule in rules.keys():
            r1_s = rules[rule][0][0]
            r1_e = rules[rule][0][1]
            r2_s = rules[rule][1][0]
            r2_e = rules[rule][1][1]
            if (val >= r1_s and val <= r1_e) or (val >= r2_s and val <= r2_e):
                valueValidForSomeRule = True
                break

        if not valueValidForSomeRule: 
            errorScanningRate += val
            numInvalid += 1
            ticketValid = False

    if ticketValid:
        validTickets.append(t)

print(f'Invalid Tickets     = {numInvalid}')
print(f'Error Scanning Rate = {errorScanningRate}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
def ruleMet(rule, val):
    r1_s = rule[0][0]
    r1_e = rule[0][1]
    r2_s = rule[1][0]
    r2_e = rule[1][1]
    if (val >= r1_s and val <= r1_e) or (val >= r2_s and val <= r2_e):
        return True
    else:
        return False

dbgPrint(validTickets)

possibleFields = []
for i in range(len(myTicket)):
    possibleFields.append([])
    for k in rules.keys():
        possibleFields[i].append(k)

dbgPrint(possibleFields)

# Get list of valid fields based upon field values
for i in range(len(myTicket)):
    # check against my ticket
    for r in possibleFields[i]:
        if not ruleMet(rules[r], myTicket[i]):
            possibleFields[i].remove(r)

    # check against all tickets
    for t in validTickets:
        for r in possibleFields[i]:
            if not ruleMet(rules[r], t[i]):
                possibleFields[i].remove(r)

    dbgPrint(f'{i}: {possibleFields[i]}')

# get list of found rules
foundRules = []
for i in range(len(myTicket)):
    if len(possibleFields[i]) == 1: 
        foundRules.append(possibleFields[i][0])

dbgPrint(f'Found Rules = {foundRules}')

# Reduce
onePossibilityPerRule = False
iteration = 0
while not onePossibilityPerRule:
    onePossibilityPerRule = True
    for i in range(len(myTicket)):
        if len(possibleFields[i]) == 1:  continue
        else:
            onePossibilityPerRule = False
            for r in foundRules:
                if r in possibleFields[i]:
                    possibleFields[i].remove(r)

            if len(possibleFields[i]) == 1:
                foundRules.append(possibleFields[i][0])

    dbgPrint(f'---- Iter {iteration} ---')
    dbgPrint(f'Found Rules = {foundRules}')
    for i in range(len(myTicket)):
        dbgPrint(f'{i}: {possibleFields[i]}')

    iteration+=1

dbgPrint(possibleFields)

multVal = 1
for i in range(len(myTicket)):
    if re.match('departure.*', possibleFields[i][0]):
        multVal *= myTicket[i]

print(f'Mult Val = {multVal}')

