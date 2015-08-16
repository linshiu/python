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

def mergeSort2(ls):
    """ Sort a list using merge sort. The idea is to break down the list 
    into halves (until 1 item in the list) and then merge recursively to sort.
    No use of slice operator.
    Args:
        ls (list): list to sort
    Returns:
        None: modifies the list
        
    """ 
    
    _mergeSort2(ls, start = 0, end = len(ls))

def _mergeSort2(ls, start, end):
    """ Sort a list using merge sort. The idea is to break down the list 
    into halves (until 1 item in the list) and then merge recursively to sort.
    No use of slice operator.
    Args:
        ls (list): list to sort
        start (int): starting pointer
        end (int): ending pointer (lenght of list)
        
    Returns:
        None: modifies the list
        
    """    
    
    # base case: stop recursive calls when 1 item in list
    if end - start > 1:
        
        # split in halves
        mid = (start + end)//2
        
        # recursive call to merge sort
        _mergeSort2(ls, start = start, end = mid)
        _mergeSort2(ls, start = mid, end = end)

        # sort
        i = start # index for left half
        j = mid # index for right half
        k = start # index for merged list
        
        temp = list(ls) # not good
        
        # iterate until all elements of right or left are inserted in list
        while i < mid and j < end:
            
            # insert from left, advance to next element of left
            if temp[i] < temp[j]:
                ls[k] = temp[i]
                i+= 1
                
            # insert from right, advance to next element of right
            else:
                ls[k] = temp[j]
                j+= 1
            
            # advance to next element in list
            k+= 1
                
        # insert remainng elements if any for left
        while i < mid:
            ls[k] = temp[i]
            i+= 1
            k+= 1                
        
        # insert remainng elements if any for right
        while j < end:
            ls[k] = temp[j]
            j+= 1
            k+= 1     
    
    #print(str(start)+"-"+str(end))
    #print(ls)

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
    
    mergeSort2(testList1)
    testList2.sort()
    
    assert testList1 == testList2
    
    print("Test: Success")  

if __name__ == "__main__":

    test()
        
    func= [mergeSort2]
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