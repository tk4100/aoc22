# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:12:16 2022

@author: nasan
"""

simVals = []            # List of lists with form [cycle #, register X value]
simVals.append([1,1])   # Start simulation at cycle 1, X register = 1
i = 1

# Generate simulation results from input file
with open("input.txt") as fh:
    for line in fh:
        inputs = line.strip().split()
        cmd = inputs[0]
        if cmd == 'noop':
            # Next cycle holds same value as previous
            simVals.append([i+1,simVals[i-1][1]])
            i += 1
        elif cmd == 'addx':
            # Next cycle holds same value as previous, but
            # the following cycle adds addx value
            number = int(inputs[1])
            simVals.append([i+1,simVals[i-1][1]])
            simVals.append([i+2,simVals[i-1][1]+number])
            i += 2

# Part 1
total = 0
for i in [20,60,100,140,180,220]:
    total += i*simVals[i-1][1]
print(f'Sum of signal strengths (P1) = {total}')

# Part 2
printString = ''
for i in range(len(simVals)):
    pos = simVals[i][0] - 1    # Drawn position = cycle - 1
    smid = simVals[i][1]       # Sprite mid point
    if pos % 40 >= smid - 1 and pos % 40 <= smid + 1:
        # Drawn position within sprite 3 pixel range (lit)
        printString += '#'
    else:
        # Dark
        printString += '.'
print(f'\nPart 2:\n')
for i in range(6):
    print(f'{printString[40*i:40*i+39]}')