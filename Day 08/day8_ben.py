# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:59:42 2022

@author: nasan
"""
# Using complex plane quadrant IV as coordinate system for trees
#
# Dictionaries to direct flow of looking through forest from all 4 sides
#              UP                 DOWN              LEFT               RIGHT
startdict = {0:complex(0,-98),  1:complex(0,0),   2:complex(98,0),  3:complex(0,0)}
indirdict = {0:complex(0,1),  1:complex(0,-1), 2:complex(-1,0), 3:complex(1,0)}
outdirdict = {0:complex(1,0),  1:complex(1,0), 2:complex(0,-1),3:complex(0,-1)}

class Tree():
    def __init__(self, row, col, height):
        self.height = height
        self.row = row
        self.col = col
        self.visible = [False, False, False, False]
        self.visScore = 0
        
    def checkBlocked(self, diridx, maxheight):
        if self.height <= maxheight:
            self.visible[diridx] = False
        else:
            self.visible[diridx] = True
            
def atBoundary(idx, loc):
    # True if at boundary and about to step out
    if loc.real == 0 and indirdict[idx].real == -1:
        return True
    elif loc.real == 98 and indirdict[idx].real == 1:
        return True
    elif loc.imag == 0 and indirdict[idx].imag == 1:
        return True
    elif loc.imag == -98 and indirdict[idx].imag == -1:
        return True
    else:
        return False

trees = {}
row = 0

# Build up forest grid (using complex plane quad IV to index dictionary)
with open("input.txt") as fh:
    for line in fh:
        cleanline = line.strip()
        for col in range(len(cleanline)):
            trees.update({complex(col,row):Tree(row,col,int(cleanline[col]))})
        row -= 1
        
# Iterate over 4 sides of square using dictionaries to direct flow
for i in range(4):
    # Iterate over outer rows/columns
    for k in range(99):
        maxheight = -1
        #Iterate over inner rows/columns
        for l in range(99):
            treeInd = startdict[i] + indirdict[i]*l + outdirdict[i]*k
            
            # Check whether the tree's view is blocked (updates self record of visibility from direction)
            trees[treeInd].checkBlocked(i,maxheight)
            if trees[treeInd].height > maxheight:
                # Update max height seen from outside
                maxheight = trees[treeInd].height
                if maxheight == 9:
                    # No more can be visible from this direction
                    break

totalVis = 0  
maxVisScore = 0                
for loc, tree in trees.items():
    # Count total visible from outside for Part 1
    if True in tree.visible:
        totalVis += 1
    
    # Compute the visibility score for each tree    
    visScore = 1
    # Loop over each direction (using indirdict to move each direction)
    for i in range(4):
        # Re-initialize values
        dirVis = 1
        dirDone = False
        viewLoc = loc
        while not dirDone and not atBoundary(i,viewLoc):
            viewLoc += indirdict[i]
            # Add to vis score if not at boundary and tree is shorter than ref tree
            if not atBoundary(i,viewLoc) and trees[viewLoc].height < tree.height:
                dirVis += 1
            else:
                dirDone = True
        visScore *= dirVis
    tree.visScore = visScore
    if visScore > maxVisScore:
        maxVisScore = visScore
        maxLoc = loc
       
# Part 1
print(f'Total visible trees = {totalVis}')

# Part 2
print(f'Maximum visibility score = {maxVisScore} @ {maxLoc}')
        
    
        