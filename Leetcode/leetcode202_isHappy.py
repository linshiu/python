# -*- coding: utf-8 -*-
"""

Leetcode - 202 - Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 

Starting with any positive integer, replace the number by the sum of the 
squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""
#%%
def isHappy(n):
    """ 
    :type n: int
    :rtype: bool
    """
    
    nStr = str(n)
   
    happy = False
    observed = False
    observedSet = set()
    
    # iterate until number = 1 or number previously observed (cycle)
    while not happy and not observed:
        nStr = str(sum([int(i)**2 for i in nStr]))

        if nStr == '1':
            happy = True
        
        elif nStr in observedSet:
            observed = True
            
        else:
            observedSet.add(nStr)
              
    return happy
    
    
#%%

test = 19
print(isHappy(test))     

test = 30
print(isHappy(test))   

test = 7
print(isHappy(test))   