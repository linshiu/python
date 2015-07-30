# -*- coding: utf-8 -*-
"""
@author: Steven Lin
"""
import itertools
import numpy as np

# Algorithm:
# "ij,jk->i,k" a,b
# split by -> into left and right
# split left by ,
# for each matrix, store labels and locations
# for each matrix, if label aready exists, raiser error

# create an array with zeros with dimensions equal to right 
# 3 Nested for loop
# loop through all tuple combinations labels in right
# Loop through all tuple combinations labels in set(all) - set(right)
# Loop through each matrix
# multiply matrices passing tuples of labels, with dictionary pulling correct locations
# sum multiplications

# the only part I couldn't get to work was creating the dictionary and
# passing labels as tuples in the loops


#%%


## function 

def einsum(substrings,*operands):
    # check operands >= 1
    substrings = substrings.strip().replace(" ","")
    left, right = substrings.split("->")
    subs = left.split(",") # list of indices of arrays
    
    substrings = substrings.replace("->",",")
    substringsList = substrings.split(",")
    
    # get unique lables
    labels = substrings.replace(",","")
    labels = "".join(set(labels))

    
    N = len(operands)
    dimLs =[]
    
    # check same letters same dimension
    # assuming the same for now
    for i in range(N):
        t = zip(subs[i],operands[i].shape)
        dimLs.extend(t)
            
    dimDic=dict(dimLs) # key: label ('i'), value: dimension (5)
    
    # instead of creating this, might be better to just
    # create an np array and the reshape to dimensions 
    
    dimRanges = [range(dimDic[k]) for k in labels]
    comb = itertools.product(*dimRanges) # np.indices((3,3))
    
    # initialize array on the right
    # note that this way retains order of list in 'right'
    indexRight = tuple([dimDic[k] for k in right])
    result = np.zeros(indexRight) 
    
    # for each tuple combination of indices
    for c in comb:
        
        index = dict(zip(labels,c))
        indexResult =  tuple([index[k] for k in right])
        
        #print(index)
        #print(indexResult)
        
        multiply = 1
        
        # for each array multiply
        for i in range(N):
            
            indexArray = tuple([index[k] for k in substringsList[i]])         
            multiply *= operands[i][indexArray]
            
            #print(indexArray)
            #print(multiply)
    
        result[indexResult] += multiply
        
    return result
        

#%% testing 

# try to replicate np.einsum('ij,jk->ik', a,b)
import itertools
import numpy as np
a = np.arange(25).reshape(5,5)
b = np.arange(25).reshape(5,5)

print(einsum('ij,jk->ik', a,b))
print(np.einsum('ij,jk->ik', a,b))

print(einsum('ij,jk->', a,b))
print(np.einsum('ij,jk->', a,b))


#%% brainstorming

# try to replicate np.einsum('ij,jk->ik', a,b)
import itertools
import numpy as np
a = np.arange(25).reshape(5,5)
b = np.arange(25).reshape(5,5)
dimA = a.shape
dimB = b.shape
p = [range(dimA[0]), range(dimB[1])]
    

comb = list(itertools.product(*p))
common = range(dimA[1])

new = np.zeros(dimA[0]*dimB[1]).reshape(dimA[0],dimB[1])

for i,k in comb:
    for j in common:
        new[(i,k)] += a[(i,j)]*b[(j,k)]
        
print(new)        
print(np.einsum('ij,jk->ik', a,b))

    


#%%

# testing
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html

import numpy as np
a = np.arange(25).reshape(5,5)
b = np.arange(5)
c = np.arange(6).reshape(2,3)

np.einsum('ii', a)

np.einsum(a, [0,0])

np.trace(a)


np.einsum('ii->i', a)

np.einsum(a, [0,0], [0])

np.diag(a)


#%% Lecture Notes

a = np.arange(30).reshape(2,3,5)
b = np.ndarray([[2,3],[4,5],[6,7]])

a = np.array([10,17,12])
b = np.array([1,2,3])
c = np.einsum("i,i -> i", a,b)

# appears on the left but not on the right -> sum
# repeated letters need to have the same length
# 'ij,jk->ki (matrix multiplication and then transpose)

# adding 1 to integer number, but + doesn't work
# count, over 9, go to the 10's 
# don't know how many digits going to have
# run out of these balls, go to do next
# bayesian network
# make code flexible 

# sum everything : "ab->"
# "ab,ab -> ab" sum corresponding elements
# "ab,ab -> " sum all

# A = [1,2]
# B = [2,3,4]

# Aa Bb = []

