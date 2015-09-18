# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 2 - recurPower
Python 2.7

In Problem 1, we computed an exponential by iteratively executing successive
multiplications. We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes base^exp by recursively
calling itself to solve a smaller version of the same problem, 
and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥0. It should return one numerical value. 
Your code must be recursive - use of the ** operator or 
looping constructs is not allowed.

"""

#%%

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    if exp <= 0:
        return 1
    
    return base*recurPower(base, exp-1)
    
    

    
#%%
    
recurPower(9.33, 0)
recurPower(3.26, 3)    