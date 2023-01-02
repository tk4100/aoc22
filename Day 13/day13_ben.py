# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:34:39 2023

@author: nasan
"""

import itertools
from enum import Enum

class result(Enum):
    same = 0
    left = 1
    right = 2

def checkOrder(pair):
    for v1,v2 in zip(pair[0],pair[1]):
        res = checkVals(v1,v2)
        if res == result.left:
            return False
        elif res == result.right:
            return True
    if len(pair[0]) > len(pair[1]):
        return False
    elif len(pair[0]) < len(pair[1]):
        return True
    else:
        raise KeyError(f'All same and same length? Is this possible?      {pair[0]}       {pair[1]}')

def checkVals(v1,v2):
    if type(v1) == int and type(v2) == int:
        # Just compare the values and return the result
        if v1 < v2:
            return result.right
        elif v1 > v2:
            return result.left
        else:
            return result.same
    elif type(v1) == int and type(v2) == list:
        # Call again as two lists
        return checkVals([v1],v2)
    elif type(v1) == list and type(v2) == int:
        # Call again as two lists
        return checkVals(v1,[v2])
    elif type(v1) == list and type(v2) == list:
        # Iterate over all values and return the value if they're not the same
        for i1,i2 in zip(v1,v2):
            res = checkVals(i1,i2)
            if res != result.same:
                return res
        # Check for length sameness (zip iterator only runs to min length)
        if len(v1) > len(v2):
            return result.left
        elif len(v1) < len(v2):
            return result.right
        else:
            return result.same
        
def sortPackets(packList):
    # This sorts the passed list in place using the checkOrder function criteria
    for i in range(len(packList)-1):
        lowest = packList[i]
        lowidx = i
        for j in range(i+1,len(packList)):
            if not checkOrder([lowest,packList[j]]):
                lowest = packList[j]
                lowidx = j
        temp = packList[i]
        packList[i] = lowest
        packList[lowidx] = temp
            

#================================================================
#================================================================
#================================================================
#================================================================

idx = 0
lnum = 0
pairs = []
correctPairs = []
allPackets = []
allSorted = []

# Populate pairs list from file
with open("input.txt") as fh:
    for line in fh:
        if lnum % 3 == 0:
            pairs.append([])
            pairs[idx].append(eval(line))
        if lnum % 3 == 1:
            pairs[idx].append(eval(line))
            idx += 1
        lnum += 1
# Part 1 - Check for correctly ordered pairs
for pnum in range(len(pairs)):
    if checkOrder(pairs[pnum]):
        # Add pnum+1 to list of correct pairs (pnum is zero indexed, but pair numbering is not)
        correctPairs.append(pnum+1)
print(f'Sum of correct pair numbers is {sum(correctPairs)}')

# Part 2
# Compile all packets together (including divider packets)
for pair in pairs:
    allPackets.append(pair[0])
    allPackets.append(pair[1])
allPackets.append([[2]])
allPackets.append([[6]])
sortPackets(allPackets)
x1 = allPackets.index([[2]]) + 1
x2 = allPackets.index([[6]]) + 1
print(f'Dividers found at {x1} and {x2}, so decoder key = {x1*x2}')
