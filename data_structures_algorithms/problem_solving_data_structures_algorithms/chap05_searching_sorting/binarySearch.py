# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3

Binary search

"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def binarySearch(ls,item):
    """ Search if item is in list
    
    Idea is to keep track of left and right indices, compute the midpoint, 
    and update left and right after comparing value from list to item so that
    at each iterationthe problem size is halved by eliminating values that 
    are not necessary to compare with. 
    
    Args:
        ls (list): list of integers in order
        item (int): integer to search
        
    Returns:
        boolean: True if found, False otherwise
        
    """
    found = False
    left  = 0
    right = len(ls)-1
    
    # iterate until pointers match    
    while left <= right and not found:
        
        mid = (left + right)//2 
        
        if item == ls[mid]:
            found = True
        
        # item is in first half of list, so discard all items greater than mid
        elif item < ls[mid]: 
            right = mid -1
            
        # item is in second half of list, so discard all less or equal than mid
        else:
            left = mid + 1
    
    return found
#%% Function #################################################################

def binarySearchR(ls,item):
    """ Search if item is in list (recursive immplementation)
    
    Reduce the list by half recursively by comparing if greather and or less 
    than the midpoint value and eliminating values that 
    are not necessary to compare with. 
    
    Args:
        ls (list): list of integers in order
        item (int): integer to search
        
    Returns:
        boolean: True if found, False otherwise
        
    """
    
    mid = len(ls)//2    #midpoint
     
    # Base case  empty, then item not found
    if len(ls)==0:
        return False
    
    # Item found
    elif item == ls[mid]:
        return True
    
    # Item not found yet, keep looking
    else:
        if item < ls[mid]:
            return binarySearchR(ls[:mid], item) # look in first half
        else:
            return binarySearchR(ls[mid+1:], item) # look in second half
        
    

#%%  Testl #################################################################
def test():
    """ Test if functions are working properly by using assertions
    
    Args:
        None
    
    Returns:
        None: will print Test: Success if everything ok, otherwise 
        assertion error
    
    """
    testList = [ 0, 2, 6, 7, 9, 15, 23, 26, 29, 50, 79]
    
    for t in testList:
        assert binarySearchR(testList, t) == True
   
    assert binarySearchR(testList, testList[0] - 1) == False
    assert binarySearchR(testList, testList[-1] + 1) == False
    assert binarySearchR(testList, 1) == False
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
    func= [binarySearch, binarySearchR]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(5):
            size = 10**(n+1)
            item = nprnd.randint(size*3)
            testList = nprnd.randint(low=0, high = size, size = size)
            
            t = timeit.Timer("{f}(testList,item)".format(f=f),
                             "from __main__ import {f}, testList, item".format(f=f))
                             
            times[f].append((size, t.timeit(number=1000)))
    
        x,y = zip(*times[f])
        plt.plot(x,y,'.-', c=np.random.rand(3,1))
        
    plt.legend([f.__name__ for f in func], loc='upper left')
    plt.ylabel('miliseconds')
    plt.xlabel('size')
    plt.show()
        



