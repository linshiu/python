# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 6 - gcdRecur
Python 2.7

Although Python provides a built-in function for computing the length 
of a string, we can write our own.

Write an iterative function, lenIter, which computes the length of an 
input argument (a string), by counting up the number of characters in the string.

"""

#%%

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    count = 0
    for ch in aStr:
        count+=1
    
    return count


    
#%%
    
lenIter("hello")