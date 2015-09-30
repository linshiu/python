# -*- coding: utf-8 -*-
"""

Leetcode - 283 - Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

#%% Method 1: not very efficient since remove searches for 0 from beginning of list each time
def moveZeroes1(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    #indicesZeroes = [i for i,v in enumerate(nums) if v == 0]
    nZeroes = nums.count(0)
    
    for i in range(nZeroes):
        nums.remove(0) 
    
    nums.extend([0]*nZeroes)

#%% Method 2:
def moveZeroes2(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    n = len(nums)
    nZeroes = 0
    i = 0
    
    while i < n:
        if nums[i] == 0:
            nZeroes += 1
            del nums[i]
            n = n-1
        else:
            i+=1
    
    nums.extend([0]*nZeroes)
    
#%%
    
nums = [0, 1, 0, 3, 12]
moveZeroes2(nums)

print(nums)
