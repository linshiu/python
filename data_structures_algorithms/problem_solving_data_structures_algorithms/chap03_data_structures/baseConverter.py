# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 3: Basic Data Structures
Convert Decimal to any base up to 16

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


#%% ##### Converting Decimal Numbers to Any Base #######################
#%% My Function

def baseConverter(decnumber, base):
    """ Convert a Decimal Number to Number in input base
    
    Use similar idea as divide by 2 algorithm with slight modification to
    take into account representations for base > 10 and include alphabetical
    characters for remainders greater than 10 (e.g. rem = 15 -> F)
    
    Args:
        decnumber (int): Decimal Number
        base(int): Base number between 2 and 16
    
    Returns:
        str: Number representaiton in new base
    """
    digits = [str(i) for i in range(10)] + [chr(i) for i in range(65,71)]
    s = Stack()
    baseStr = ""
    
    # store remainder in stack after subsequent division by 2
    while decnumber > 0:
        remainder = decnumber % base
        decnumber = decnumber//base
        s.push(digits[remainder])
    
    # create binary string by removing items in stack
    while not s.isEmpty():
        baseStr += str(s.pop())
        
    return baseStr
    

#%% Test

print(baseConverter(25,2))
print(baseConverter(25,16))
print(baseConverter(25,8))
print(baseConverter(10995,16))
print(baseConverter(256,16))
