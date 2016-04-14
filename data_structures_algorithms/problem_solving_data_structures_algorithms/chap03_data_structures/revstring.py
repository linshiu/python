# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 3: Basic Data Structures

IDE: Spyder, Python 3

Reverse a string using a stack

"""

from datastructures import Stack

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

if __name__ == "__main__":
    
	print (revstring('apple') == 'elppa')
	print (revstring('x') == 'x')
	print (revstring('1234567890') == '0987654321')
	print (revstring('stressed'))