# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:59:10 2022

@author: BAW28893
"""

import string

# Lowercase alphabetical array for assigning value for hill heights
valueList = list(string.ascii_lowercase)

class Point():
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.parent = []
        self.hchar = height
        self.height = self.getHeight(height)
        self.visited = False
  
    def getHeight(self, char):
        if char == 'S':
            return 0
        elif char == 'E':
            return 25
        else:
            # return the value from a lowercase alphabetical array
            return valueList.index(char)
      
class Hill():
    def __init__(self):
        self.points = []
        self.start = []
        self.end = []
        self.queue = []
        
    def addToQueue(self,point,currpt):
        # Add point to end of queue
        self.queue.append(point)
        # Set parent to point adding to queue
        point.parent = currpt
        # Mark as visited, so it's not added by other neighboring points
        point.visited = True             
   
    def findEnd(self):
        # Initialize the queue
        self.queue.append(self.start)
        self.start.visited = True
        foundEnd = False
        
        # Run through queue, adding as we go (BFS)
        while not foundEnd and self.queue:
            # Take point at the front of the queue (FIFO)
            currpt = self.queue[0]
            row = currpt.row
            col = currpt.col
            # OPTIONAL PRINT LINE TO KNOW WHERE YOU ARE
            #print(f'currpt = {row}, {col}')   
            if currpt != self.end:
                # Check all neighboring points for existence, visited, and height
                if row + 1 < len(self.points):
                    if not self.points[row+1][col].visited:
                        if self.points[row+1][col].height <= currpt.height + 1:
                            # Add neighbor to the queue
                            self.addToQueue(self.points[row+1][col],currpt)
                if row - 1 >= 0:
                    if not self.points[row-1][col].visited:
                        if self.points[row-1][col].height <= currpt.height + 1:
                            # Add neighbor to the queue
                            self.addToQueue(self.points[row-1][col],currpt)
                if col + 1 < len(hill.points[row]):
                    if not self.points[row][col+1].visited:
                        if self.points[row][col+1].height <= currpt.height + 1:
                            # Add neighbor to the queue
                            self.addToQueue(self.points[row][col+1],currpt)
                if col - 1 >= 0:
                    if not self.points[row][col-1].visited:
                        if self.points[row][col-1].height <= currpt.height + 1:
                            # Add neighbor to the queue
                            self.addToQueue(self.points[row][col-1],currpt)
                # Pop current point off the queue
                self.queue.pop(0)
            else:
                # Wooo found it! Exit the loop.
                foundEnd = True 
               
    def countStepsFromChar(self, char):
        # Finds the number of steps to get to the end point from the last
        # point of a given char level
        
        # Initialize, starting at the end point
        count = 0
        currPt = self.end
        
        # Make sure the end point has a parent already (is found)
        if self.end.parent:
            # Loop over each subsequent parent, checking for desired height char
            while currPt.hchar != char:
                currPt = currPt.parent
                count += 1
            return count
        else:
            raise KeyError(f'Hill Object .end does not have a parent!')
      
#================================================================
#================================================================
#================================================================
#================================================================
            
hill = Hill()
row = 0   

# Populate hill structure with points/heights from input file
with open("input.txt") as fh:
    for line in fh:
        cleanline = line.strip()
        hill.points.append([])
        for col in range(len(cleanline)):
            # Build array (list) of points (row, col, height)
            hill.points[row].append(Point(row,col,cleanline[col]))
            if cleanline[col] == 'S':
                # Save start point for easy reference
                hill.start = hill.points[row][col]
            elif cleanline[col] == 'E':
                # Save end point for easy reference
                hill.end = hill.points[row][col]
        row += 1

# Use BFS search to find the shortest path to end point
hill.findEnd()

# Part 1
numStepsFromS = hill.countStepsFromChar('S')
print(f'Number of steps to get to end point = {numStepsFromS}')
# Part 2
numStepsFromA = hill.countStepsFromChar('a')
print(f'Number of steps from last \'a\' = {numStepsFromA}')
            
            
            
      
      