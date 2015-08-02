# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 3: Basic Data Structures
Convert Decimal to Binary

IDE: Sypder, Python 3.0

"""
#%% ##### Stack Immplementation ##############################################
#%% My Stack Immplementation

class Stack:
        def __init__(self):
            self.items =[]
            
        def isEmpty(self):
            return self.items == []
            
        def size(self):
            return len(self.items)
            
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            return self.items.pop()
            
        def peek(self):
            return self.items[len(self.items)-1]       

#%% Test Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


#%% ##### Converting Decimal Numbers to Binary Numbers #######################
#%% My Function

def divideBy2(decnumber):
    """ Convert a Decimal Number to Binary Number
    
    Use the Divide by 2 algorithm. Divide successively number by 2 every time
    until division results in 0. Store remainder at every step (value of 1 or 0)
    Binary representation is the 1 or 0 's in reverse order computed.
    
    Args:
        decnumber (int): Decimal Number
    
    Returns:
        str: Binary representaiton.
    """
    s = Stack()
    binaryStr = ""
    
    # store remainder in stack after subsequent division by 2
    while decnumber > 0:
        remainder = decnumber % 2
        decnumber = decnumber//2
        s.push(remainder)
    
    # create binary string by removing items in stack
    while not s.isEmpty():
        binaryStr += str(s.pop())
        
    return binaryStr

#%% Test

print(divideBy2(42))