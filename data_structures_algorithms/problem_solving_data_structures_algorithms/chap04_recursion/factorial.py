# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 4: Recursion

IDE: Spyder, Python 3

Compute factorial using recursion

"""
import math
#%% Function ################################################################

def factorial(n):
    """ Compute factorial
    
    Args:
        n (int): integer to compute factorial
    
    Regturns:
        int: factorial
    
    """

    if n <= 1:
        return 1
    
    else:
        return n*factorial(n-1)
        
#%% test ####################################################################

def test():
    testList = [0,1,2,3,4]
    
    for n in testList:
        assert factorial(n) == math.factorial(n)

    print("Test: Success")


if __name__ == "__main__":

    test()