# -*- coding: utf-8 -*-
"""
Leetcode 205 - Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        mapping = {}
        seen_t = set()
        
        
        i = 0
        mismatch = False
        
        while i < len(s) and not mismatch:
            
            # new letter, so add to mapping
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
                
                # check mapping unique
                mismatch = (t[i] in seen_t)
                seen_t.add(t[i])
            
            # if letter seen before, then check the mapping is the same
            else:
                mismatch = (mapping[s[i]] != t[i])
            
            i+=1
                
        # no mismatch --> isomorphic is True
        return not mismatch
            
#%% Alternative:
class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """            
            
        d1 = {}
        d2 = {}
        
        for i in range(len(s)):
            
            d1[s[i]] = d1.get(s[i],i)
            d2[t[i]] = d2.get(t[i],i)
            
            if d1[s[i]] != d2[t[i]]:
                return False
        
        return True
        
#%% Test ####################################################################
        
if __name__ == "__main__":
    test = Solution()
    
    cases = {("egg","add"):True,
             ("foo","bar"):False,
             ("paper","title"):True,
             ("ab","aa"): False}
    
    for case in cases:
        assert test.isIsomorphic(*case) == cases[case]