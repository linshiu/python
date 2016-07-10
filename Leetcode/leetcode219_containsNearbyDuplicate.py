# -*- coding: utf-8 -*-
"""

Leetcode - 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there
are two distinct indices i and j in the array such that nums[i] = nums[j]
and the difference between i and j is at most k.


Time: O(n)
Space: O(n)

Iterate list, adding the value as key, and the index as value in dictionary
If already seen element, then check if difference in index and stored index is 
less or equal to k. Return True if this is the case, otherwise update index
of element in dictionary.

"""

#%% Function ##################################################################
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # key = value of nums, value = index of array
        dic = {}
        
        for index, num in enumerate(nums):
            
            if num in dic:
                
                if index - dic[num] <= k:
                    return True
                
                else:
                    dic[num] = index
                
            else:
                dic[num] = index
                
        return False


        
#%% Test #####################################################################
        
if __name__ == "__main__":
    test = Solution()
    
    nums = [4,2,5,0,3,4,3]
    k = 2
    
    print(test.containsNearbyDuplicate(nums,k))
    
    nums = [4,2,5,0,3,4,3]
    k = 1
    
    print(test.containsNearbyDuplicate(nums,k))
    
    