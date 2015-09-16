# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 1 - iterPower
Python 2.7

Write an iterative function iterPower(base, exp) that calculates the 
exponential baseexp by simply using successive multiplication. 
For example, iterPower(base, exp) should compute baseexp by multiplying 
base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer >= 0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed.

"""

#%%

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    if exp == 0 or base == 1:
        return 1
    
    if base == 0:
        return 0
    
    result = base
    
    while exp > 1:
        result *= base
        exp -= 1
      
    return result
    
#%%
    
iterPower(9.33, 0)
iterPower(3.26, 3)    