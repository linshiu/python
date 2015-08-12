# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Selection Sort
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def insertionSort(ls):
    """ Sort a list using selection sort
    
    Make passes through the list until list is sorted. Assume start with a 
    sublist with only the first item. In each pass, compare the next item 
    in the list to the ones in the sublist, and shift items right until correct
    position found to insert item.
    
    Args:
        ls (list): list to sort
        
    Returns:
        None: modifies the list
        
    """    
    
    n = len(ls)
    
    # passes (up to n-1) 
    for nPass in range(n-1):

        # iterate until nPass-1 comparisons in sublist or found insertion location
        i = nPass
        new = ls[nPass + 1]
             
        while i >= 0 and new < ls[i]:
            
            # shift to the right
            ls[i+1] = ls[i]
            
            i-=1
        
        ls[i+1] = new

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
    
    insertionSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
  
    func= [insertionSort]
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