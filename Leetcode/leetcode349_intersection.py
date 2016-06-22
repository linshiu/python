# -*- coding: utf-8 -*-
"""
Leetcode 349 - Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.


"""

#%% Solution 1
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    common = []
    nums1 = set(nums1)
    nums2 = set(nums2)
    
    if len(nums1) < len(nums2):
        for n1 in nums1:
            if n1 in nums2:
                common.append(n1)
    else:
        for n2 in nums2:
            if n2 in nums1:
                common.append(n2)
        
    return common

#%% Solution 2

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    
    return list(nums1.intersection(nums2))
    
#%% Test
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

intersection(nums1,nums2)
    