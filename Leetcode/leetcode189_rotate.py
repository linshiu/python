# -*- coding: utf-8 -*-
"""

Leetcode 189 - Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

Solution1: 
Use queue, pop from end and insert beginning k%len(nums) times

Solution2:
Use slicing, remove the last k%len(nums) elements and append to beginning


Time: O(n)
Space: O(1)


"""

#%% First solution: queue
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # new position: (i+k)%n
        
        # take into account shift > n, which repeat... (k = n, complete rotation, so like no shifts )
        shifts = k%len(nums)
        
        # remove from end and insert at beginning
        while shifts > 0:
            end = nums.pop()
            nums.insert(0,end)
            shifts-=1
        
 #%% First solution: queue
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # new position: (i+k)%n
        
        # take into account shift > n, which repeat... (k = n, complete rotation, so like no shifts )
        shifts = k%len(nums)
        
        # remove the last shifts elements (e.g. shifts = 2, get the last 2) and append to beginning
        if shifts != 0: 
            nums[:] = nums[-shifts:] + nums[:-shifts]
            # first array slice from end shifts values, 
            # second array slice from beginning up to shift values from end
        
        
        
#%% Test #####################################################################
        
if __name__ == "__main__":
    test = Solution2()
    ls = [0,1,2]
    k = 4
    
    test.rotate(ls,k)
    print(ls)
    
    