# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L4 PROBLEM 9 - Odd
Python 2.7

Write a Python function, odd, that takes in one number and 
returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.


"""

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    
    return not (x%2 == 0)
    #return x%2==1
    
    
print (odd(4))
print (odd(5))