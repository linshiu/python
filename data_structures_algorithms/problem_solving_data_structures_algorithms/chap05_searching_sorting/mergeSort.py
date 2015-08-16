# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Merge Sort
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

def mergeSort(ls):
    """ Sort a list using merge sort. The idea is to break down the list 
    into halves (until 1 item in the list) and then merge recursively to sort. 
    Args:
        ls (list): list to sort
        
    Returns:
        None: modifies the list
        
    """    
    
    # base case: stop recursive calls when 1 item in list
    if len(ls) > 1:
        
        # split in halves
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        
        # recursive call to merge sort
        mergeSort(left)
        mergeSort(right)
    
        # sort
        i = 0 # index for left half
        j = 0 # index for right half
        k = 0 # index for merged list
        
        # iterate until all elements of right or left are inserted in list
        while i < len(left) and j < len(right):
            
            # insert from left, advance to next element of left
            if left[i] < right[j]:
                ls[k] = left[i]
                i+= 1
                
            # insert from right, advance to next element of right
            else:
                ls[k] = right[j]
                j+= 1
            
            # advance to next element in list
            k+= 1
                
        # insert remainng elements if any for left
        while i < len(left):
            ls[k] = left[i]
            i+= 1
            k+= 1                
        
        # insert remainng elements if any for right
        while j < len(right):
            ls[k] = right[j]
            j+= 1
            k+= 1     
    


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
    
    mergeSort(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
  
    func= [mergeSort]
    times = {f.__name__: [] for f in func}
    
    for f in times:
        
        for n in range(4):
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