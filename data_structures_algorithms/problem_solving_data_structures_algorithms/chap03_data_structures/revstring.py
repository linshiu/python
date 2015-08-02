# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 3: Basic Data Structures

IDE: Spyder, Python 3

Reverse a string using a stack

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

#%% ##### Reverse characters using stack #####################################
#%% My Function

def revstring(mystr):
    '''  Reverse the characters in a string using a stack
    
    Args:
        mystr (string): string to reverse
    
    Returns:
        string: reversed string
    
    '''
    
    s = Stack()
    revmystr = ""
    
    for ch in mystr:
        s.push(ch)
    
    while not s.isEmpty():
        revmystr += s.pop()
    
    return revmystr
    
#%% Test
    
print (revstring('apple') == 'elppa')
print (revstring('x') == 'x')
print (revstring('1234567890') == '0987654321')
print (revstring('stressed'))