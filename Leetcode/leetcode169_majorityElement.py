# -*- coding: utf-8 -*-
"""

Leetcode 169. Majority Element

Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.

@author: Steven
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        frequency = {}
        
        for element in nums:
            frequency[element] = frequency.get(element,0) + 1
            if frequency[element] > len(nums)//2:
                return element
        
        
        
        
#%% Test
        
if __name__ == "__main__":
    test = Solution()
    test.majorityElement(["A","B","B","A","B","C"])