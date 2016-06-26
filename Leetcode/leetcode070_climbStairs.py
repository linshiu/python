# -*- coding: utf-8 -*-
"""

Leetcode 70. -  Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 

In how many distinct ways can you climb to the top?

Solution:

Think like a decision treen starting at n, next level can take 1 step (n-1) or 
2 steps (n-2). Continue branching out until reach either 0 or 1, then the number
of leaves is the number of distinct ways to get to n with 1 or 2 steps.

"""

class Solution(object):
    
    def __init__(self):
        self.found = {}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 or n == 1:
            return 1
        
        if n in self.found:
            return self.found[n]
        
        combinations = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.found[n] = combinations
        return  combinations
        
        
class Solution2(object):
    
    # adapted from kamyu104
    def climbStairs(self, n):
        
        # initialize
        previous = 0
        current = 1
        
        for i in range(n):
            
            #update
            # f(n) = f(n-1) + f(n-2)
            
            previous, current = current, previous + current 
        
        return current
             

        
#%% Test #####################################################################
        
if __name__ == "__main__":
    
    test = Solution()
    cases = {0: 1,
             1: 1,
             2: 2,
             3: 3,
             4: 5,
             5: 8}
    for case in cases:
        assert test.climbStairs(case) == cases[case]
    