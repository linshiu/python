# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Quick Sort
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np
import random
#%% Function #################################################################

def quickSort(ls):
    """ Sort a list using quick sort. Sort elements with respect to a pivot
    in each pass. After a pass, split list in two based on pivot and repeat
    quick sort on each recursively until no sublist to sort. 
    
    Args:
        ls (list): list to sort
    Returns:
        None: modifies the list
        
    """ 
    
    _quickSort(ls, start = 0, end = len(ls))

def _quickSort(ls, start, end):
    """ Sort a list using quick sort. Sort elements with respect to a pivot
    in each pass. After a pass, split list in two based on pivot and repeat
    quick sort on each recursively until no sublist to sort. 
    
    Args:
        ls (list): list to sort
        start (int): starting pointer
        end (int): ending pointer (lenght of list)
        
    Returns:
        None: modifies the list
        
    """   
    if end - start > 1:  # nothing to sort if the range has less than 2 elements
        pivot = partition(ls, start, end)
        _quickSort(ls, start, pivot)
        _quickSort(ls, pivot, end)
                
def partition(ls, start, end):
    '''Function  will rearrange in place the elements of l in the range [i:j]
    into two nonempty ranges [i:q] and [q:j] such that each element in
    l[i:q] is less than or equal to each element l[q:j].
    
    Args:
        ls (list): , is a mutable indexable object (e.g. a list or numpy array).
        start (int): start index
        end (int): end index
    
    Returns:
        q (int): index q is returned 
    
    '''

    # partition value
    pivot = ls[random.randint(start, end-1)]
    # other option try median

    # define pointers moving from start (left) and end (right)
    left = start
    right = end-1

    # iterate until left and right pointers cross
    while left <= right:

        # advance left pointer until value greater or equal than pivot
        while ls[left] < pivot:
            left += 1

        # advance right pointer until value less or equal than pivot
        while ls[right]> pivot:
            right -= 1

        # swap if in wrong side of pivot
        if left <= right:
            ls[left], ls[right] = ls[right], ls[left]
            left +=1
            right-=1

    return left            
        

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
    
    quickSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
    func= [quickSort]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(5):
            size = 3**(n+1)
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