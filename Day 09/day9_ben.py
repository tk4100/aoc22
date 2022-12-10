# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:43:58 2022

@author: nasan
"""

class Knot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.locs = set()
        self.locs.add(tuple([self.x, self.y]))
        
    def getPos(self):
        return [self.x, self.y]
    
    def moveKnot(self, direction):
        # Move knot in all directions in direction string
        # - Should handle diagonal motion for U/D+R/L motion for tail
        if 'R' in direction:
            self.x += 1
        if 'L' in direction:
            self.x -= 1
        if 'U' in direction:
            self.y += 1
        if 'D' in direction:
            self.y -= 1
        self.locs.add(tuple([self.x, self.y]))
        
def calcDisp(a, b):
    # a and b are Knot objects which return position as [x,y] list
    aPos = a.getPos()
    bPos = b.getPos()
    diff = [aPos[0]-bPos[0], aPos[1]-bPos[1]]
    return diff

knots = []
for i in range(10):
    knots.append(Knot())

with open("input.txt") as fh:
    for line in fh:
        inputs = line.strip().split()
        headdir = inputs[0]
        number = int(inputs[1])
        
        # Loop for number of head moves in each direction
        for i in range(number):
            knots[0].moveKnot(headdir)
            for j in range(1,10):    
                disp = calcDisp(knots[j-1], knots[j])
                if abs(disp[0]) > 1 or abs(disp[1]) > 1:
                    # Move tail
                    taildir = ''
                    if disp[0] > 0:
                        taildir = taildir + 'R'
                    if disp[0] < 0:
                        taildir = taildir + 'L'
                    if disp[1] > 0:
                        taildir = taildir + 'U'
                    if disp[1] < 0:
                        taildir = taildir + 'D'
                    knots[j].moveKnot(taildir)

# Part 1
print(f'Number of Knot 1 locations (P1) = {len(knots[1].locs)}')
# Part 2
print(f'Number of tail locations (P2) = {len(knots[9].locs)}')