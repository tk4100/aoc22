# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:03:08 2022

@author: BAW28893
"""

class Monkey():
    def __init__(self,name,kind,value):
        self.name = name
        self.kind = kind
        self.isfromhuman = False
        if kind == "val":
            self.value = value
        elif kind == "eqn":
            # Break 'value' list into individual parts
            self.var1 = value[0]
            self.op = value[1]
            self.var2 = value[2]
        else:
            raise KeyError(f'Unknown Monkey kind {kind}')
        
    def getVal(self):
        
        # Return own value, recursively get inputs if necessary
        if self.kind == "val":
            return self.value
        elif self.kind == "eqn":
            val1 = Monkeys[self.var1].getVal()
            val2 = Monkeys[self.var2].getVal()
            if self.op == '+':
                return int(val1 + val2)
            elif self.op == '-':
                return int(val1 - val2)
            elif self.op == '*':
                return int(val1 * val2)
            elif self.op == '/':
                return int(val1 / val2)
            else:
                raise KeyError(f'Unknown equation operator {self.op}')
                
    def calcUnknown(self):
        
        # Figure out which is known/unknown
        if Monkeys[self.var1].isfromhuman:
            unknown = Monkeys[self.var1].name
            known = Monkeys[self.var2].name
            knum = 2
        else:
            unknown = Monkeys[self.var2].name
            known = Monkeys[self.var1].name
            knum = 1
            
        # Get the result and known value (argument)
        result = self.value
        arg = Monkeys[known].getVal()
        
        # Compute unknown value by inversing operation
        if self.op == '+':
            Monkeys[unknown].value = int(result - arg)
        elif self.op == '-':
            if knum == 2:
                Monkeys[unknown].value = int(result + arg)
            else:
                Monkeys[unknown].value = int(arg - result)
        elif self.op == '*':
            div = result / arg
            Monkeys[unknown].value = int(div + result % div)
        elif self.op == '/':
            if knum == 2:
                Monkeys[unknown].value = int(result * arg)
            else:
                Monkeys[unknown].value = int(arg / result)
            
        # Continue calling this function if this didn't compute the 'humn' item
        if unknown != "humn":
            Monkeys[unknown].calcUnknown()
    
    def fromHuman(self):
        # Figure out if self or Monkeys down the chain are the human
        if self.name == 'humn':
            # Human
            self.isfromhuman = True
        elif self.kind == 'val':
            # Non-human value
            self.isfromhuman = False
        else:
            # If either variable is in the chain, this is in the chain
            v1 = Monkeys[self.var1].fromHuman()
            v2 = Monkeys[self.var2].fromHuman()
            self.isfromhuman = v1 or v2 
        
        return self.isfromhuman
        
#================================================================
#================================================================
#================================================================
#================================================================        
    
Monkeys = {}

# Build up dictionary of Monkeys from input file
with open('input.txt') as fh:
    for line in fh:
        words = line.strip().split()
        name = words[0].replace(':','')
        
        if len(words) == 2:
            # Add val to dictionary
            Monkeys[name] = Monkey(name,'val',int(words[1]))
        elif len(words) == 4:
            # Add eqn to dictionary
            Monkeys[name] = Monkey(name,'eqn',[words[1],words[2],words[3]])
        else:
            raise KeyError(f'Unexpected line length {len(words)}')

# Part 1 - Get value of root Monkey
rootVal = Monkeys['root'].getVal()
print(f'Part 1: Value of root Monkey = {rootVal}')

# Part 2
rm1 = Monkeys[Monkeys['root'].var1].getVal()
rm2 = Monkeys[Monkeys['root'].var2].getVal()
if rm1 != rm2:
    # Get trace up of path from Human
    Monkeys['root'].fromHuman()
    
    # Figure out which monkey under root is unknown
    if Monkeys[Monkeys['root'].var1].isfromhuman:
        rootUnknown = Monkeys[Monkeys['root'].var1].name
        rootKnown = Monkeys[Monkeys['root'].var2].name
    else:
        rootUnknown = Monkeys[Monkeys['root'].var2].name
        rootKnown = Monkeys[Monkeys['root'].var1].name
    # Calculate unknown values from root down to human
    Monkeys[rootUnknown].value = Monkeys[rootKnown].getVal()
    Monkeys[rootUnknown].calcUnknown()
    
    # Print humn value
    humanVal = Monkeys['humn'].value
    print(f'Part 2: Human value = {humanVal}')
else:
    print(f'Part 2: Human value is already good!' )
    humanVal = Monkeys['humn'].value
    print(f'   value = {humanVal}')
    


