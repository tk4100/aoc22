# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:30:37 2022

@author: BAW28893
"""

import math

snafuMult = [-2, -1, 0, 1, 2]
snafuChar = ['=', '-', '0', '1', '2']

def valFromSnafu(inp):
    if inp == '-':
        return -1
    elif inp == '=':
        return -2
    else:
        return int(inp)

def decFromSnafu(line):
    linesum = 0
    for i in range(len(line)):
        linesum += decFromFivePlace(i,line[len(line)-1-i])
    return linesum

def decFromFivePlace(place,val):
    return valFromSnafu(val) * 5 ** place

def listMult(num,lst):
    return [num*value for value in lst]

def listDiff(num,lst):
    return [num-value for value in lst]

def listAbs(lst):
    return [abs(value) for value in lst]

def snafuIdx(exp,num):
    localVals = listMult(5**exp,snafuMult)
    localDiffs = listDiff(num,localVals)
    localDiffAbs = listAbs(localDiffs)
    minAbs = min(localDiffAbs)
    return localDiffAbs.index(minAbs)

def snafuFromDec(num):
    snafu = ''
    initExp = int(math.log(num,5))
    if num > 2.4*5**initExp:
        initExp += 1
    for i in range(initExp+1):
        exp = initExp - i
        idx = snafuIdx(exp,num)
        num -= snafuMult[idx]*5**exp
        snafu += snafuChar[idx]   
    return snafu

total = 0
with open("input.txt") as fh:
    for line in fh:
        cleanline = line.strip()
        decimal = decFromSnafu(cleanline)
        print(decimal, snafuFromDec(decimal))
        total += decimal
        
# Part 1
snafu = snafuFromDec(total)
print(f'SNAFU input to Bob is {snafu}')