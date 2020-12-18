#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

operations = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    operations.append(line.strip())
inputFile.close()
dbgPrint(operations)

print("------------------")
print("---- PART 1 ------")
print("------------------")
runningSum = 0
for o in operations:
    curVals = [0]
    curOps  = ['+']
    for idx in range(0,len(o)):
        if o[idx] == " ": continue

        # number found
        if re.match('\d', o[idx]):
            val = int(o[idx])
            if curOps[-1] == '+':
                curVals[-1] += val
            if curOps[-1] == '*':
                curVals[-1] *= val

        # operator
        if re.match('[\+\*]', o[idx]):
            curOps[-1] = o[idx]

        # Open Paren
        if o[idx] == "(":
            curVals.append(0)
            curOps.append('+')

        if o[idx] == ")":
            val = curVals.pop()
            curOps.pop()

            if curOps[-1] == '+': curVals[-1] += val
            if curOps[-1] == '*': curVals[-1] *= val

    runningSum += curVals[0]

print(f'Sum = {runningSum}')


print("------------------")
print("---- PART 2 ------")
print("------------------")

runningSum = 0
for o in operations:
    opStr = list(o.replace(' ',''))
    for i in range(len(opStr)):
        if opStr[i].isdigit():
            opStr[i] = int(opStr[i])

    dbgPrint(f'INIT:  {opStr}')

    while len(opStr) > 1:
        ##### ADDITION #####
        add = False
        popIdxs = []
        for i in range(len(opStr)-2):
            if isinstance(opStr[i], int) and opStr[i+1] == '+' and isinstance(opStr[i+2], int):
                val = opStr[i] + opStr[i+2]
                popIdxs.append(i+1)
                popIdxs.append(i+2)
                opStr[i] = val
                add = True
                break

        for i in reversed(popIdxs):
            opStr.pop(i)

        if add: 
            dbgPrint('ADD:   ', end='')
            dbgPrint(opStr)
            continue

        ##### MULTIPLY #####

        # In Parens
        popIdxs = []
        mult = False
        for i in range(len(opStr)):
            if opStr[i] == '(':
                parensIsInner = True
                onlyMultiply  = True
                multiplySeen  = False
                for j in range(i+1,len(opStr)):
                    if opStr[j] == "(":
                        parensIsInner = False
                        onlyMultiply  = False
                        break
                    if opStr[j] == '+':
                        onlyMultiply  = False
                        break
                    if opStr[j] == ")":
                        break
                    if opStr[j] == '*':
                        multiplySeen = True

                if parensIsInner and onlyMultiply and multiplySeen:
                    val = opStr[i+1] * opStr[i+3]
                    opStr[i+1] = val
                    popIdxs.append(i+2)
                    popIdxs.append(i+3)
                    mult = True
                    break

        for i in reversed(popIdxs):
            opStr.pop(i)

        if mult:
            dbgPrint('MUL1:  ', end='')
            dbgPrint(opStr)
            continue
            
        # Outside Parens - Final Ops
        popIdxs = []
        mult = False
        if len(opStr) > 1 and opStr[1] == '*':
            for i in range(len(opStr)-1):
                onlyMultiply  = True
                if opStr[i] == "(":
                    onlyMultiply  = False
                    break
                if opStr[i] == '+':
                    onlyMultiply  = False
                    break

            if onlyMultiply:
                val = opStr[0] * opStr[2]
                opStr[0] = val
                popIdxs.append(1)
                popIdxs.append(2)
                mult = True

        for i in reversed(popIdxs):
            opStr.pop(i)

        if mult:
            dbgPrint('MUL2:  ', end='')
            dbgPrint(opStr)
            continue

        ##### REMOVE PARENS #####
        popIdxs = []
        parens = False
        for i in range(len(opStr)-2):
            if opStr[i] == '(' and opStr[i+2] == ')':
                popIdxs.append(i+0)
                popIdxs.append(i+2)
                parens=True

        for i in reversed(popIdxs):
            opStr.pop(i)

        if parens:
            dbgPrint('PAREN: ', end='')
            dbgPrint(opStr)
            continue


    runningSum += opStr[0]

print(f'Sum = {runningSum}')


