# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:22:46 2022

@author: nasan
"""

# Select Part 1 or Part 2 for number of rounds and worry value calc
Part = 1   # 1 or 2 

if Part == 1:
    numRounds = 20
    worryDiv = 3
elif Part == 2:
    numRounds = 10000
    worryDiv = 1
else:
    raise KeyError(f'Invalid Part: {Part}')

class Monkey():
    def __init__(self, items, op, opVal, testVal, tMonkey, fMonkey):
        self.items = items
        self.op = op
        self.opVal = opVal
        self.testVal = testVal
        self.tMonkey = tMonkey
        self.fMonkey = fMonkey
        self.numItemsProcessed = 0
        
    def processItem(self, item):
        # Increment number of items processed
        self.numItemsProcessed += 1
        if self.opVal == 'old':
            val = item
        else:
            val = int(self.opVal)
        
        # Perform operation on item
        if self.op == '+':
            item += val
        elif self.op == '*':
            item *= val
        else:
            raise KeyError(f'Op type {self.op} not recognized!')
            
        # Divide by 3 (rounding down) for Part 1, 1 (no change) for Part 2
        item //= worryDiv
        
        #Perform test on value to decide where to pass it
        if item % self.testVal == 0:
            return [item % LCM, self.tMonkey]
        else:
            return [item % LCM, self.fMonkey]

    def processAllItems(self):
        passItems = []
        for item in self.items:
            passItems.append(self.processItem(item))
        self.items = []
        
        return passItems
        

def passItems(toPass):
    for pItem in toPass:
        monkeys[pItem[1]].items.append(pItem[0])
    
        
monkeys = []

# Process inputs and create Monkeys
with open("input.txt") as fh:
    for line in fh:
        inputs = line.strip().split()
        
        # Process inputs by line content and create Monkey at blank line
        if not inputs:
            pass
        elif inputs[0] == 'Monkey':
            # not actually necessary since monkeys are in order
            mNum = int(inputs[1].replace(':',''))    
        elif inputs[1] == 'items:':
            items = []
            for i in range(2,len(inputs)):
                items.append(int(inputs[i].replace(',','')))
        elif inputs[0] == 'Operation:':
            op = inputs[4]
            opVal = inputs[5]
        elif inputs[0] == 'Test:':
            testVal = int(inputs[3])
        elif inputs[1] == 'true:':
            tMonkey = int(inputs[5])
        elif inputs[1] == 'false:':
            fMonkey = int(inputs[5])
            # Create Monkey object after false: line since it is the last for each Monkey
            monkeys.append(Monkey(items,op,opVal,testVal,tMonkey,fMonkey))

# Calculate LCM for worry management
LCM = 1
for monkey in monkeys:
    LCM *= monkey.testVal

# Run 20/10000 rounds
for i in range(numRounds):
    print(f'Running round {i}!')
    # Run each monkey in order per round
    for j in range(len(monkeys)):
        #print(f'   Running Monkey {j}')
        # Process all items and then pass to other monkeys
        toPass = monkeys[j].processAllItems()
        passItems(toPass)

# Part 1/2
mNums = []
for i in range(len(monkeys)):
    mNums.append(monkeys[i].numItemsProcessed)
mNums.sort()
monkeyBusiness = mNums[len(mNums)-1]*mNums[len(mNums)-2]
print(f'MonkeyBusiness score = {monkeyBusiness}')
                