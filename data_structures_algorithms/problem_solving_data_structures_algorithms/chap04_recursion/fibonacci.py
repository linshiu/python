# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 4: Recursion

IDE: Spyder, Python 3

Write a recursive function to compute the Fibonacci sequence. 
How does the performance of the recursive function compare to that of an iterative version?

"""

import timeit
import matplotlib.pyplot as plt

#%% Function #################################################################
def fibonacciLoop(n):
    """ Find the Fibonacci sequence using loop
    
    Defined as the sum of the previous values of the sequence
    
    F(n) = F(n-1) + F(n-2)
    Where F(0) = 0, F(1) = 1
    
    Args:
        n (int): positive integer for an index in sequence
    
    Regturns:
        int: fibonacci value for that index in sequence
    
    """
    
    n_1, n_2 = 1, 0
    
    if n == 0:
        return 0
    
    for i in range(n-1):
        n_1, n_2 = n_1 + n_2, n_1
        
        
    return n_1
        
#%% Function #################################################################
def fibonacciRecursive(n):
    """ Find the Fibonacci sequence using recursion
    
    Defined as the sum of the previous values of the sequence
    
    F(n) = F(n-1) + F(n-2)
    Where F(0) = 0, F(1) = 1
    
    Args:
        n (int): positive integer for an index in sequence
    
    Regturns:
        int: fibonacci value for that index in sequence
    
    """
    
    
    if n<=1:
        return n
        
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

#%% Function #################################################################
known = {0: 0, 1: 1} # base

def fibonacciMemoization(n):
    """ Find the Fibonacci sequence using memoization
    
    Defined as the sum of the previous values of the sequence
    
    F(n) = F(n-1) + F(n-2)
    Where F(0) = 0, F(1) = 1
    
    More efficient to keep track of values already calculated so don't
    have to recalculate
    
    Args:
        n (int): positive integer for an index in sequence
    
    Regturns:
        int: fibonacci value for that index in sequence
    
    """
    
    if n not in known:
        known[n] = fibonacciMemoization(n-1) + fibonacciMemoization(n-2)
    return known[n]

#%%  Testl #################################################################

'''
FIBONACCI_LIST = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
                      1597,2584,4181,6765,10946,17711,28657,46368,75025,
                      121393,196418,317811,514229,832040,1346269,
                      2178309,3524578,5702887,9227465,14930352,24157817,
                      39088169]
'''
FIBONACCI_LIST = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]

def test():
    FIBONACCI_LIST = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
    
    for n in range(len(FIBONACCI_LIST)):
        F = FIBONACCI_LIST[n]
        assert fibonacciLoop(n) == F
        assert fibonacciRecursive(n) == F
        assert fibonacciMemoization(n) == F
    
    print("Test: Success")

if __name__ == "__main__":

    test()
        
    times = {"fibonacciLoop": [],
             "fibonacciRecursive": [],
             "fibonacciMemoization": []}
    
    known = {0: 0, 1: 1} 
    
    for f in times:

        times[f] = [timeit.Timer("{f}({n})".format(f=f,n=n),
                    "from __main__ import {f}, FIBONACCI_LIST, known".format(f=f))
                    .timeit(number=1000) for n in range(len(FIBONACCI_LIST))]
    
    x = range(len(FIBONACCI_LIST))
    plt.plot(x,times["fibonacciLoop"],'.r-')
    plt.plot(x,times["fibonacciRecursive"],'.g-')
    plt.plot(x,times["fibonacciMemoization"],'.b-')
    plt.legend(["fibonacciLoop","fibonacciRecursive", "fibonacciMemoization"], loc='upper left')
    plt.ylabel('miliseconds')
    plt.xlabel('fibonacci')
    plt.show()
