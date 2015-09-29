# -*- coding: utf-8 -*-
"""
Leetcode 242 - isAnagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""

#%%
def getFrequency(s):
    """ Returns a dictionary with key= character, value= frequency
    Assumes string is composed of lower case string characters
    
    Args:
        s (str): string of characters
    
    Returns:
        dict: dictionary key = character, value = frequency
    """    
    
    freq = {chr(i): 0 for i in range(97,122+1)}
    
    for ch in s:
        freq[ch] += 1
            
    return freq
    
#%%
def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sFreq = getFrequency(s)
        tFreq = getFrequency(t)
        
        for ch in s:
            if sFreq[ch] != tFreq[ch]:
                return False
        
        return True
        
#%%
s = "anagram"
t = "nagaram"  

print(isAnagram(s,t))

s = "rat"
t = "car"

print(isAnagram(s,t))