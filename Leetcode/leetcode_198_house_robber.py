# -*- coding: utf-8 -*-
"""

Leetcode - 198 - House Robber

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security
system connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


Solution:

Time: O(n)
Space: O(n)

Dynamic programming solution by saving subproblem solutions

A[i] = money in ith house
B[i] = max money for i houses
B[0] = 0
B[1] = A[i]

for house i, there are 2 cases:
1) Don't rob i th house, and rob best combination for the first i-1 houses
2) Rob ith house, and rob best combination for the first i-2  houses 
   (since house i-1 th cannot be robbed since house is ith is robbed and cannot be consecutive)

B[i] = max(0 + B[i-1], A[i]+B[i-2])


"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        # key: # houses, value: max money
        best = {0:0, 1:nums[0]}
        
        # i = number of houses
        for i in range(2,len(nums)+1):
            best[i] = max(best[i-1],nums[i-1]+best[i-2]) # note nums[0] -> first house
            
        return best[len(nums)]
            
        
        
        
#%% Test #####################################################################
        
if __name__ == "__main__":
    
    test = Solution()
    print(test.rob([2,10,3,4])) # 14 (NYNY)
    print(test.rob([10,2,2,10])) # 20 (YNNY)
    