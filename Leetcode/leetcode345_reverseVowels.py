# -*- coding: utf-8 -*-
"""
Leetcode - 345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Solution:

Move left pointer to right and right pointer to left until find vowels, then
swap. Keep moving pointers until cross.

Time: O(n)
Space: O(n)

"""



#%% Solution #################################################################

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = {'a','e','i','o','u', 'A', 'E', 'I', 'O','U'}
        
        left = 0
        right = len(s) - 1
        
        ls = list(s)
        
        while left < right:
            
            # move left pointer to right until find a vowel
            if ls[left] not in vowels:
                left+=1
            
            # move right pointer to left until find a vowel
            if ls[right] not in vowels:
                right-=1
            
            # if both a vowel then swap and move pointers
            if ls[left] in vowels and ls[right] in vowels:
                
                ls[left], ls[right] = ls[right], ls[left]
                
                left+=1
                right-=1
                
        
        return "".join(ls)
        
        
        
        
#%% Test #####################################################################
        
if __name__ == "__main__":
    
    test = Solution()
    cases = {"hello": "holle", "leetcode": "leotcede", "m": "m", "qq": "qq", "soy": "soy", 'Aa':'aA'}
    
    for word in cases:

        assert test.reverseVowels(word) == cases[word]