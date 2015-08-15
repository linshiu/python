# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Shell Sort
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def shellSort(ls):
    """ Sort a list using shell sort. The idea is to break down the list 
    into sublists with items apart by a gap. Sort each sublist and repeat
    by changing the gap until the sublist = fulllist (gap = 1).
    
    Args:
        ls (list): list to sort
        
    Returns:
        None: modifies the list
        
    """    

    n = len(ls)
    
    gap = n // 2  # number of sublists = gap
    
    # iterate until number of sublists = 1
    while gap > 0:
        
        # iterate each sublist
        for start in range (gap):  # start = starting point of sublist
            insertionSortGap(ls, start, gap) # sort sublist
        
        gap = gap // 2 # reduce the number of sublists

def insertionSortGap(ls, start, gap):
    """ Sort sublist using insertion sort
    
    Make passes through the sublist until sublist is sorted. Assume start with a 
    sublist with only the first item. In each pass, compare the next item 
    in the list to the ones in the sublist, and shift items right until correct
    position found to insert item.
    
    Args:
        ls (list): full list
        start (int): index of starting point of sublist
        gap (int): 
    
    Returns:
        None: modifies the list

    """    
    n = len(ls)
    
    # passes 
    # iterate sublist in increments = gap (stop n-gap since getting start + gap)
    for nPass in range(start,n-gap,gap):
        
        # iterate until comparisons done in sublist or found insertion location
        i = nPass
        new = ls[nPass + gap]
             
        while i >= start and new < ls[i]:
            
            # shift to the right
            ls[i+gap] = ls[i]
            
            i-=gap
        
        ls[i+gap] = new

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
    
    shellSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
  
    func= [shellSort]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(3):
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