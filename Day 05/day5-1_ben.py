# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:07:26 2022

@author: BAW28893
"""

def moveCrate(slist, num, origin, dest):
   for i in range(num):
      slist[dest].append(slist[origin].pop(len(slist[origin])-1))

'''
============================================================================        
============================================================================        
============================================================================        
'''

parsing = True 
stacks = [ [] for i in range(10)]     
with open("input5") as fh:
   # Parse inputs
   for line in fh:
      if parsing and line[0:10] == ' 1   2   3':
         # Done parsing initial configuration
         parsing = False
         for i in range(9):
            stacks[i+1].reverse()
      if parsing:
         # Continue parsing initial configuration
         for i in range(9):
            if line[4*i + 1] != ' ':
               stacks[i+1].append(line[4*i + 1])
      else:
         # Split the rest and move some crates!
         splitline = line.strip().split()
         if splitline and splitline[0] == 'move':
            num = int(splitline[1])
            origin = int(splitline[3])
            dest = int(splitline[5])
            moveCrate(stacks, num, origin, dest)
               
# Part 1
outstr = ''
for i in range(9):
   outstr+=stacks[i+1][len(stacks[i+1])-1]
print(outstr)   

          
        