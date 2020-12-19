#!/usr/bin/python

import sys
import re
import copy

debug = False
def dbgPrint(string, end='\n'):
    if debug: print(string, end=end)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Rule:
    def __init__(self):
        self.num = 0
        self.deps = []
        self.vals = []

rules = {}
messages = []
resolvedRules = []
unresolvedRules = []
inputMode = 'rules'
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if line == "\n":
        inputMode = 'messages'
        continue

    if inputMode == 'rules':
        m = re.match('^(\d+): (.*)', line)
        ruleNum = int(m.group(1))
        ruleStr = m.group(2)
        ruleDeps = []
        for c in ruleStr.split():
            if c.isdigit() and not int(c) in ruleDeps:
                ruleDeps.append(int(c))

        rules[ruleNum] = {'resolved':False, 'deps':ruleDeps, 'rule': ruleStr, 'vals':[]}
        unresolvedRules.append(ruleNum)

    if inputMode == 'messages':
        messages.append(line.strip())

inputFile.close()

rulesOrig      = copy.deepcopy(rules)
unresolvedOrig = copy.deepcopy(unresolvedRules)
resolvedOrig   = copy.deepcopy(resolvedRules)

print("------------------")
print("---- PART 1 ------")
print("------------------")

while not rules[0]['resolved']:
    dbgPrint(unresolvedRules)
    dbgPrint("-------------")
    # Find rule that is not resolved, but all deps satisfied
    for u in unresolvedRules:
        r = rules[u]
        if len(r['deps']) == 0:
            # initial letter
            if r['rule'][0] == "\"" and r['rule'][2] == "\"":
                r['vals'] = [r['rule'][1]]
                r['resolved'] = True
                unresolvedRules.remove(u)
                resolvedRules.append(u)

            # Resolve complex rule
            else:
                vals = []
                rulesToPermute = []
                # get rule nums to permute
                for idx,c in enumerate(r['rule'].split()):
                    if c.isdigit():
                        rulesToPermute.append(int(c))

                    if c=="|" or idx == len(r['rule'].split()) - 1:
                        permuteList = []
                        for p in rulesToPermute:
                            permuteList.append(rules[p]['vals'])

                        # clear out for next pipe
                        rulesToPermute = []
                        
                        if len(permuteList) == 1: permuteList.append([""])
                        if len(permuteList) == 2: permuteList.append([""])

                        for a in permuteList[0]:
                            for b in permuteList[1]:
                                for c in permuteList[2]:
                                    r['vals'].append(a+b+c)

                r['resolved'] = True
                unresolvedRules.remove(u)
                resolvedRules.append(u)

            # remove rule from other deps
            for d in unresolvedRules:
                if u in rules[d]['deps']: rules[d]['deps'].remove(u)


    for r in rules:
        dbgPrint(rules[r])

print("matching messages...")

regexP1 = "^("
regexP1 +="|".join(rules[0]['vals'])
regexP1 += ")$"
regexP1c = re.compile(regexP1)

numMatch = 0
for m in messages:
    if regexP1c.match(m):
        numMatch += 1

print(f'Num Matches = {numMatch}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

#0: 8 11
#8: 42 | 42 8
#11: 42 31 | 42 11 31

regex42 = "^("
regex42 +="|".join(rules[42]['vals'])
regex42 += ")$"
regex31 = "^("
regex31 +="|".join(rules[31]['vals'])
regex31 += ")$"

regex42c = re.compile(regex42)
regex31c = re.compile(regex31)

ruleLen = len(rules[42]['vals'][0])

numMatch = 0
for m in messages:
    if len(m) % ruleLen != 0: continue

    num42 = 0
    for i in range(0,len(m), ruleLen):
        subStr = m[i:i+ruleLen]
        if not regex42c.match(subStr): break
        num42+=1

    if num42 < 2: continue

    num31 = 0
    fullMatch = True
    for j in range(i,len(m), ruleLen):
        subStr = m[j:j+ruleLen]
        if not regex31c.match(subStr):
            fullMatch = False
            break;
        num31+=1

    if not fullMatch: continue
    if num31 > (num42 - 1): continue

    numMatch+=1

print(f'Num Matches = {numMatch}')



