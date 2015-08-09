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
        self.size = 11
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
            hashValue = self.rehashFunction(hashValue, self.size)
            
            # iterate until either find an empty slot or same key to replace
            while self.keys[hashValue] != None and self.keys[hashValue] != key:
                hashValue = self.rehashFunction(hashValue, self.size)
                    
            if self.keys[hashValue] == None:
                self.keys[hashValue] = key
                self.values[hashValue] = value
            
            else:
                self.values[hashValue] = value
                
    def get(self, key):
        
        hashValue = self.hashFunction(key,self.size)
        orginalHashValue = hashValue
        
        found = False
        checkAll = False
        value = None
        
        # iterate until hash value is not present, or hash value is present
        # and same key, or check all slots and not found
        while self.keys[hashValue] != None and not found and not checkAll:
            
            if self.keys[hashValue] == key:
                found = True
                value = self.values[hashValue]
                
            else:
                hashValue = self.rehashFunction(hashValue, self.size)
                
                if hashValue == orginalHashValue:
                    checkAll = True
                
        return value
        
    def hashFunction(self, key, size):
        return key%size
        
    def rehashFunction(self, oldHashValue, size):
        return (oldHashValue + 1)%size
        
    def __setitem__(self,key, value):
        self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)
        
    def pairs(self):
        return [(k,v) for (k,v) in zip(self.keys, self. values) if k != None]
        
    def __str__(self):
        return str(["{key}: {value}".format(key =k, value = v) for (k,v) in self.pairs()])
    
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
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.keys)
    print(H.values)
        

    H[20]='duck'
    print(H[20])

    print(H.values)
    print(H[99])
    print(H.pairs())
    print(H)
    
if __name__ == "__main__":

    test()
        