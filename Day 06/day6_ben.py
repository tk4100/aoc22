# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:03:34 2022

@author: BAW28893
"""

def checkForDups(chars):
   duplicates = [char for char in chars if chars.count(char) > 1]
   if duplicates:
      return True
   else:
      return False

packetindex = 4
packetfound = False   
msgindex = 14
msgfound = False
with open("input6") as fh:   
   for line in fh:
      while not packetfound:
         if not checkForDups(line[packetindex-4:packetindex]):
            packetfound = True
         else:
            packetindex += 1
      while not msgfound:
         if not checkForDups(line[msgindex-14:msgindex]):
            msgfound = True
         else:
            msgindex += 1      
      
            
print(f'Packet index = {packetindex}')
print(f'Message index = {msgindex}')