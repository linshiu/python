# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Hash function for string
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def hashString(string, tableSize):
    """ Hash function for string
    
    Convert characters to ordinal values, weigh by position, sum up,
    return remainder    
    
    Args:
        string (str): string of characters
        tableSize (int): size of table 

    Returns:
        int : hash value        
        
    """
    total = 0
    for pos in range(len(string)):
        total += ord(string[pos])*(pos+1)
        
    return total%tableSize



#%%  Testl #################################################################
def test():
    """ Test if functions are working properly by using assertions
    
    Args:
        None
    
    Returns:
        None: will print Test: Success if everything ok, otherwise 
        assertion error
    
    """
    print(hashString("hello", 20))
    print(hashString("hello", 20))
    print(hashString("angel", 20))
    print(hashString("glean", 20))

if __name__ == "__main__":

    test()
        