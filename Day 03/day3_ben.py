# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:23:31 2022

@author: BAW28893
"""

import string

valueList = list(string.ascii_letters)

def sameInSacks(string):
   sack1 = set(string[0:int(len(string)/2)])
   sack2 = set(string[int(len(string)/2):int(len(string))])
   return list(sack1 & sack2)[0]

def sameInGroup(strings):
   set1 = set(strings[0])
   set2 = set(strings[1])
   set3 = set(strings[2])
   return list(set1 & set2 & set3)[0]

def getValue(char):
   return valueList.index(char) + 1
   
uniqueList = []
totalUniqueValue = 0
totalBadgeValue = 0
groupLines = ['','','']
linecnt = 0
with open("input3") as fh:   
   for line in fh:
      cleanline = line.strip()
      # Part 1
      totalUniqueValue += getValue(sameInSacks(cleanline))
      
      #Part 2
      groupLines[linecnt % 3] = cleanline
      if linecnt % 3 == 2:
         totalBadgeValue += getValue(sameInGroup(groupLines))
         
      linecnt += 1
# Part 1
print(f'Total Badge Value = {totalUniqueValue}')
# Part 2
print(f'Total Badge Value = {totalBadgeValue}')
     