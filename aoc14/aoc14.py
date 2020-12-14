#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

instructions = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    mask = re.match('^mask = (.*)$', line)
    mem  = re.match('^mem\[(\d+)\] = (\d+)$', line)

    if mask:
        maskList = list(mask.group(1))
        maskList.reverse()
        instructions.append(['mask', maskList])
    if mem:
        instructions.append(['mem', int(mem.group(1)), int(mem.group(2))])

inputFile.close()

for i in instructions:
    dbgPrint(i)

print("------------------")
print("---- PART 1 ------")
print("------------------")
memMap = {}
clearMask = 2**36-1 # AND this
setMask   = 0       # OR this
for inst in instructions:
    if inst[0] == 'mask':
        clearMask = 2**36-1
        setMask   = 0
        for i in range(36):
            if inst[1][i] == '0':  clearMask = clearMask & (~(1 << i))
            if inst[1][i] == '1':  setMask   = setMask   | (1 << i)
        dbgPrint(f'setMask   = {setMask:b}')
        dbgPrint(f'clearMask = {clearMask:b}')
    if inst[0] == 'mem':
        memMap[inst[1]] = ((inst[2] & clearMask) | setMask)

memSum = 0
for i in memMap.keys():
    memSum += memMap[i]

print(f'Memory Sum = {memSum}')


print("------------------")
print("---- PART 2 ------")
print("------------------")
memMap = {}
clearMask = 2**36-1 # AND this
setMask   = 0       # OR this
floats    = []
for inst in instructions:
    if inst[0] == 'mask':
        clearMask = 2**36-1
        setMask   = 0
        floats    = []
        for i in range(36):
            #if inst[1][i] == '0':  # zeros leave address unchanged
            if inst[1][i] == '1':  setMask   = setMask   | (1 << i)
            if inst[1][i] == 'X':  
                clearMask = clearMask & (~(1 << i)) # clear float bits to zero
                floats.append(i)
        dbgPrint(f'setMask   = {setMask:b}')
        dbgPrint(f'clearMask = {clearMask:b}')
        dbgPrint(f'floats    = {floats}')

    if inst[0] == 'mem':
        address = ((inst[1] & clearMask) | setMask)

        for f in range(2**len(floats)):
            floatMsk  = 0
            for bitPos in range(len(floats)):
                bit = (f >> bitPos) & 1 
                floatMsk = floatMsk | (bit << floats[bitPos])

            dbgPrint(f'Write: mem[{address|floatMsk}] = {inst[2]}')
            memMap[address|floatMsk] = inst[2]

memSum = 0
for i in memMap.keys():
    memSum += memMap[i]

print(f'Memory Sum = {memSum}')


