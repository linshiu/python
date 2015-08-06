# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3

Sequential search

"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd

#%% Function #################################################################
def sequentialSearch(ls,item):
    """ Search if item is in list
    
    Args:
        ls (list): list of integers
        item (int): integer to search
        
    Returns:
        boolean: True if found, False otherwise
        
    """
    index = 0
    found = False
    stop = False
    N = len(ls)
    
    while index < N and not found and not stop:
        if item == ls[index]:
            found = True
        elif ls[index] > item:
            stop = True
        else:
            index+=1
    
    return found
      
        
#%%  Testl #################################################################
        
def test():
    testList = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    
    assert sequentialSearch(testList, 3) == False
    assert sequentialSearch(testList, 13) == True
    
    print("Test: Success")   
        
if __name__ == "__main__":

    test()
        
    time = []
    for n in range(5):
        size = 10**(n+1)
        item = nprnd.randint(size*3)
        testList = nprnd.randint(low=0, high = size, size = size)
        
        f = sequentialSearch.__name__
        
        t = timeit.Timer("{f}(testList,item)".format(f=f),
                         "from __main__ import {f}, testList, item".format(f=f))
                         
        time.append((size, t.timeit(number=1000)))
    
    x,y = zip(*time)
    plt.plot(x,y,'.r-')
    plt.legend([f], loc='upper left')
    plt.ylabel('miliseconds')
    plt.xlabel('size')
    plt.show()
    
    
        
