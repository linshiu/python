# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 3 - recurPowerNew
Python 2.7

The function recurPower(base, exp) from Problem 2 computed baseexp by 
decomposing the problem into one recursive case and one base case:

base^exp = base*base^(exp-1) if exp > 0
base^exp = 1 if exp = 0

Another way to solve this problem just using multiplication 
(and remainder) is to note that

base^exp = base*base^(exp-1) if exp > 0 and exp is odd
base^exp = base*base^(2)^(exp/2) if exp > 0 and exp is even
base^exp = 1 if exp = 0

Write a procedure recurPowerNew which recursively 
computes exponentials using this idea.

"""

#%%

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # base
    if exp <= 0:
        return 1
    
    # even
    elif exp%2 == 0:
        return recurPowerNew(base*base, exp/2)
      
    # odd
    else:
        return base*recurPowerNew(base, exp-1)
    
    

    
#%%
    
recurPowerNew(9.33, 0)
recurPowerNew(3.26, 3)    