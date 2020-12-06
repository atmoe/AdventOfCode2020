#!/usr/bin/python

import sys
import re

debug = False
def dbgPrint(string):
    if debug: print(string)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")

passports = []
newPassport = True
passport = {}

for line in inputFile.readlines():
    # check if blank line
    if line == "\n":
        passports.append(passport)
        passport = {}

    for field in line.split():
        [key, value] = field.split(':')
        passport[key] = value

# no new line at end of file, append last entry
passports.append(passport)

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

validpassports = 0
for p in passports:
    if 'byr' not in p.keys(): continue
    if 'iyr' not in p.keys(): continue
    if 'eyr' not in p.keys(): continue
    if 'hgt' not in p.keys(): continue
    if 'hcl' not in p.keys(): continue
    if 'ecl' not in p.keys(): continue
    if 'pid' not in p.keys(): continue

    validpassports += 1

print(f'valid passports = {validpassports}')

print("------------------")
print("---- PART 2 ------")
print("------------------")

validpassports = 0
for p in passports:
    dbgPrint(p)
    if 'byr' not in p.keys():
        continue
    elif int(p['byr']) > 2002 or int(p['byr']) < 1920:
        continue

    dbgPrint('BYR - VALID')

    if 'iyr' not in p.keys():
        continue
    elif int(p['iyr']) > 2020 or int(p['iyr']) < 2010:
        continue

    dbgPrint('IYR - VALID')

    if 'eyr' not in p.keys():
        continue
    elif int(p['eyr']) > 2030 or int(p['eyr']) < 2020:
        continue
    dbgPrint('EYR - VALID')

    if 'hgt' not in p.keys():
        continue
    else:
        cms    = re.search('(\d+)cm', p['hgt'])
        inches = re.search('(\d+)in', p['hgt'])
        if not cms and not inches: continue
        if cms    and (int(cms.group(1))    < 150 or int(cms.group(1))    > 193): continue
        if inches and (int(inches.group(1)) < 59  or int(inches.group(1)) > 76):  continue
    dbgPrint('HGT - VALID')

    if 'hcl' not in p.keys():
        continue
    else:
        hcl = re.search('^#[0-9a-f]{6}$', p['hcl'])
        if not hcl: continue
    dbgPrint('HCL - VALID')

    if 'ecl' not in p.keys(): 
        continue
    else:
        if not p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: continue
    dbgPrint('ECL - VALID')

    if 'pid' not in p.keys():
        continue
    else:
        pid = re.search('^[0-9]{9}$', p['pid'])
        if not pid: continue
    dbgPrint('PID - VALID')

    validpassports += 1

print(f'valid passports = {validpassports}')



