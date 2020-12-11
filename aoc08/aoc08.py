#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

instructions = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.match('(\w+) (.*)$', line)
    instructions.append( (m.group(1), int(m.group(2))))

inputFile.close()

for i in instructions:
    dbgPrint(i)

print("------------------")
print("---- PART 1 ------")
print("------------------")

pcHash = {}
pc = 0
accumulator = 0
revisit = False
while not revisit:
    op      = instructions[pc][0]
    operand = instructions[pc][1]
    
    if pc in pcHash:
        revisit = True
        continue
    else:
        pcHash[pc] = True

    if op == "nop":
        dbgPrint(f"PC = {pc} NOP")
        pc += 1
    elif op == "acc":
        dbgPrint(f"PC = {pc} ACC: a = {accumulator} + {operand} = {accumulator+operand}")
        accumulator += operand
        pc += 1
    elif op == "jmp":
        dbgPrint(f"PC = {pc} JMP: pc = {pc} + {operand} = {pc+operand}")
        pc += operand

print(f'Final Accumulator Value = {accumulator}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

pcsToSwap = []
for idx,i in enumerate(instructions):
    if i[0] == "jmp" or i[0] == "nop":
        pcsToSwap.append(idx)

for swapPC in pcsToSwap:
    dbgPrint(f"--- trying PC={swapPC} ---")
    revisit = False
    terminated = False
    pc = 0
    pcHash = {}
    accumulator = 0
    while not revisit and not terminated:
        op      = instructions[pc][0]
        operand = instructions[pc][1]

        if pc == swapPC:
            if   op == "nop": op = "jmp"
            elif op == "jmp": op = "nop"
    
        if pc in pcHash:
            revisit = True
            continue
        else:
            pcHash[pc] = True

        if op == "nop":
            dbgPrint(f"PC = {pc} NOP")
            pc += 1
        elif op == "acc":
            dbgPrint(f"PC = {pc} ACC: a = {accumulator} + {operand} = {accumulator+operand}")
            accumulator += operand
            pc += 1
        elif op == "jmp":
            dbgPrint(f"PC = {pc} JMP: pc = {pc} + {operand} = {pc+operand}")
            pc += operand

        if pc >= len(instructions):
            terminated = True

    if terminated: break

print(f'Final Accumulator Value = {accumulator}')




