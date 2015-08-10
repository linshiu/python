# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Bubble Sort
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def bubbleSort(ls):
    """ Sort a list using bubble sort
    
    Make passes through the list until list is sorted. During each pass,
    make comparisons between consecutive items and excahnge if out of order,
    so that items "bubble up" to the top of the list. So for the next pass, one
    fewer comparison (last) has to be made compared to the previous pass 
    because sorted values are at the top.
    Stop until n-1 passes are done, or no exchanges were made during a pass
    
    Args:
        ls (list): list to sort
        
    Returns:
        None: modifies the list
        
    """
    n = len(ls)
    i = 0
    swap = True
    
    # passes (up to n-1) and whenever no swaps made in an iteration
    while i < n-1 and swap:
        
        swap = False # reset swaps        
        # comparisons (up to n-1 for pass 0, n-2 for pass 1.. etc)
        for j in range(n-1-i):
            
            # swaps            
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                swap = True
        i+=1
            
        

#%%  Testl #################################################################
def test():
    """ Test if functions are working properly by using assertions
    
    Args:
        None
    
    Returns:
        None: will print Test: Success if everything ok, otherwise 
        assertion error
    
    """
    testList1 = [54,26,93,17,77,31,44,55,20]
    testList2 = [54,26,93,17,77,31,44,55,20]
    
    bubbleSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
    
    func= [bubbleSort]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(5):
            size = 5**(n+1)
            item = nprnd.randint(size*3, size = size)
            testList = nprnd.randint(low=0, high = size, size = size)
            
            t = timeit.Timer("{f}(testList)".format(f=f),
                             "from __main__ import {f}, testList".format(f=f))
                             
            times[f].append((size, t.timeit(number=1000)))
    
        x,y = zip(*times[f])
        plt.plot(x,y,'.-', c=np.random.rand(3,1))
        
    plt.legend([f.__name__ for f in func], loc='upper left')
    plt.ylabel('miliseconds')
    plt.xlabel('size')
    plt.show()
    