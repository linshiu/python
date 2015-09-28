# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Quiz - Problem 7
Python 2.7

Write a Python function that returns a list of keys in aDict that map to 
integer values that are unique (i.e. values appear exactly once in aDict). 
The list of keys you return should be sorted in increasing order. 
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

"""

#%% Function
def uniqueValues(aDict):
    ''' Find the keys with unique values
    
    Args:
        aDict: a dictionary
    
    Returns:
        list: keys with unique value
    '''
    # invert dictionary: key: old value, value: list of old keys 
    unique = []
    invDict = {}
    for k,v in aDict.items():
        if v not in invDict:
            invDict[v] = [k]
        else:
            invDict[v].append(k)
    
    # return unique by checking lenght = 1
    for k,v in invDict.items():
        if len(v) == 1:
            unique.append(v[0])
    
    return sorted(unique)
    
    
        
#%% Test
        
testDic = {'b':2, 'a': 1, 'e': 1, 'h':30}
print (uniqueValues(testDic))
