# -*- coding: utf-8 -*-
"""
AoC 2022 Day 7

"""

class fileSysItem ():
    """
    fileSysItem class
    
    Attributes:
    itemtype - string ('dir' or 'file')
    size - int (file sets size on init, 
                dir init to 0 then size of total contents after .getSize call)
    children - dictionary of fileSysItem objects (only dir type, N/A for file type)
    lt100k - int size if < 100k (dir only, includes sum of child dirs with size < 100k)
    
    Functions:
    getsize - returns size for 'file', returns sum of children.getsize for 'dir'
    getlt100k - rolls up lt100k sum to top level
    getFileToDelete - return size of smallest file to delete (among self and children) 
                      to free at least delSize space
    """
    
    def __init__(self, name, itemtype, size=0,children={}):
        self.itemtype = itemtype
        self.name = name
        self.lt100k = 0
        self.children = {}
        if itemtype == 'dir':
            self.size = 0
        elif itemtype == 'file':
            self.size = int(size)
            
    def getsize(self):
        if self.itemtype == 'file':
            return self.size
        elif self.itemtype == 'dir':
            totsize = 0
            for chname,chobject in self.children.items():
                totsize += chobject.getsize()
            self.size = totsize
            if self.size <= 100000:
                self.lt100k = self.size
            return totsize
        
    def getlt100k(self):
        childrensum = 0
        if len(self.children) == 0:
            pass
        else:
            for chname,chobject in self.children.items():
                childrensum += chobject.getlt100k()
        return self.lt100k + childrensum
    
    def getFileToDelete(self, delSize, currSmallest):
        if self.size >= delSize and self.size < currSmallest :
            currSmallest = self.size
            
        if len(self.children) == 0:
            pass
        else:
            for chname,chobject in self.children.items():
                currSmallest = chobject.getFileToDelete(delSize,currSmallest)
        
        return currSmallest

def updatePath(path, change):
    #print(f'updatePath: path: {path}, change: {change}')
    if change == '/':
        path = []
    elif change == '..':
        path.pop(len(path)-1)
    else:
        path.append(change)
        
def cd(path):
    global currentItem
    
#    print(f'cd: 1: {path}')
    currentItem = topDir
    if len(path) == 0:
        pass
    else:
        for dir in path:
#           print(f'cd: 2: {currentItem.name}')
#           print(f'cd: 3: {currentItem.children.keys()}')
            currentItem = currentItem.children[dir]
#    print(f'cd: 4: {currentItem.name}')
        
        
'''
============================================================================        
============================================================================        
============================================================================        
'''

totDiskSize = 70000000
diskSizeNeed = 30000000
        
topDir = fileSysItem('top','dir')
currentItem = topDir
path=[]

with open("input.txt") as fh:
    # Build up the filesystem
    for line in fh:
        stuff = line.strip().split()
        if len(stuff) == 3:
            # cd command
            updatePath(path, stuff[2])
            cd(path)            
#        elif len(stuff) == 2 and stuff[0] == '$':
#            # ls command
#            pass
        elif len(stuff) == 2 and stuff[0] != '$':
            # ls contents
            if stuff[0] == 'dir':
                # dir
                currentItem.children.update({stuff[1] : fileSysItem(stuff[1],'dir')})
            else:
                # file
                currentItem.children.update({stuff[1] : fileSysItem(stuff[1],'file',size=stuff[0])})
                
    # Update sizes across the filesystem
    topDir.getsize()
    
    # Get lt100k (part 1)
    print(f'Sum of <100k = {topDir.getlt100k()}')
    
    # Calculate sizes for part 2
    diskAvailable = totDiskSize - topDir.size
    toDelete = diskSizeNeed - diskAvailable
    
    # Get smallest file to delete (part 2)        
    print(f'Size of smallest file to delete = {topDir.getFileToDelete(toDelete, topDir.size)}')