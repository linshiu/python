# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L6 PROBLEM 7 - applyToEach
Python 2.7

Assume that

testList = [1, -4, 8, -9]

For each of the following questions (which you may assume is evaluated
independently of the previous questions, so that testList has the value
indicated above), provide an expression using applyToEach, so that after
evaluation testList has the indicated value. You may need to write a simple
procedure in each question to help with this process.



"""

#%%

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
        
    
#%% [1, 4, 8, 9]
testList = [1, -4, 8, -9]
applyToEach(testList, abs)
print(testList)


#%% [2, -3, 9, -8]

testList = [1, -4, 8, -9]
applyToEach(testList, lambda x: x+1)
print(testList)

#%% [1, 16, 64, 81]

testList = [1, -4, 8, -9]
applyToEach(testList, lambda x: x**2)
print(testList)
