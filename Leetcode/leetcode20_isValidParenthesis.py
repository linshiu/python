# -*- coding: utf-8 -*-
"""
Leetcode - 20 - Valid Parenthesis

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all 
valid but "(]" and "([)]" are not.

"""
#%% Function

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openS = '({['
    closeS = ')}]'
    openStack = [] # list simulate stack
    openDic = dict(zip(openS, closeS)) # key: open, value: close
    
    i=0
    
    # iterate entire string or until open-close do not match
    while i < len(s):
        
        # if open parenthesis, add to stack
        if s[i] in openS:
            openStack.append(s[i])
        
        # else is a close parenthesis, so invalid if no parenthesis in stack or
        # pop open parenthesis and compared to corresponding close different
        elif openStack == [] or openDic[openStack.pop()] != s[i]:
            return False
        
        i+=1
    
    if openStack == []:
        return True
    
    else:
        return False
    
    
    
#%% Test

test = "()[]{}"
print(isValid(test))

test = "([)]"
print(isValid(test))
        
test = "]"
print(isValid(test))
