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

def selectionSort(ls):
    """ Sort a list using selection sort
    
    Make passes through the list until list is sorted. During each pass,
    only exchange the largest item to the correct position. In the next pass,
    the next largest item is in the correct place.
    
    Args:
        ls (list): list to sort
        
    Returns:
        None: modifies the list
        
    """
    nPass = len(ls) - 1
    
    # passes (up to n-1) 
    while nPass > 0:
    
        maxIndex = 0       
        # comparisons (up to n-1 for 1st pass, n-2 for 2nd pass.. etc)
        for j in range(nPass):
            
            # find index with maximum value           
            if ls[j+1] > ls[maxIndex]:
                maxIndex = j+1
        
        # largest value in the pass not in place
        if maxIndex != nPass:
            ls[maxIndex], ls[nPass] = ls[nPass], ls[maxIndex]
        
        nPass-=1
            
        

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
    
    selectionSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
  
    func= [selectionSort]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(5):
            size = 2**(n+1)
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
   