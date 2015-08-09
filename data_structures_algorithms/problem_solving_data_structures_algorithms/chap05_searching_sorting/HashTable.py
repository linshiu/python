# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 5: Searching and Sorting
IDE: Spyder, Python 3
Map abstract data type
"""
import timeit
import matplotlib.pyplot as plt
import numpy.random as nprnd
import numpy as np

#%% Function #################################################################

class HashTable:
    def __init__(self):
        self.size = 15
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def put(self, key, value):
        
        hashValue = self.hashFunction(key,self.size)
        
        # case 1: key is not present, so put
        if self.keys[hashValue] == None:
            self.keys[hashValue] = key
            self.values[hashValue] = value
            
        # case 2: key is present, so replace
        elif self.keys[hashValue] == key:
            self.values[hashValue] = value
            
        # case 3: collision, so rehash and check case 2 and 3
        else:
            newHashValue = self.rehashFunction(hashValue, self.size)
            
            # iterate until either find an empty slot or same key to replace
            while self.keys[newHashValue] != None and self.keys[newHashValue] != key:
                newHashValue = self.rehashFunction(hashValue, self.size)
                    
            if self.keys[hashValue] == None:
                self.keys[hashValue] = key
                self.values[hashValue] = value
            
            else:
                self.values[hashValue] = value
            
    def hashFunction(self, key, size):
        return key%size
        
    def rehashFunction(self, oldHashValue, size):
        return (oldHashValue)%size
        
    def __setitem__(self,key, value):
        self.put(key, value)
        
    def __str__(self):
        return str(self.keys)
    
    # str vs repr
    # http://satran.in/2012/03/14/python-repr-str.html
#%%
        

        
#%%  Testl #################################################################
def test():
    """ Test if functions are working properly by using assertions
    
    Args:
        None
    
    Returns:
        None: will print Test: Success if everything ok, otherwise 
        assertion error
    
    """
    H=HashTable()
    
    
if __name__ == "__main__":

    test()
        