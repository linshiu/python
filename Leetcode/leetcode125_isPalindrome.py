# -*- coding: utf-8 -*-
"""
Leetcode 125 - Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to 
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
import re
#%%
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    # remove non-alphanumeric (including _) and convert to lower case
    s = re.sub('[^a-zA-Z0-9]','',s).lower()
        
    left = 0
    right = len(s)-1
    
    # iterate until markers from left and right cross (palindrome) or 
    # found mismatch from left and right (not palindrome)
    while left < right:
        
        if s[left] != s[right]:
            return False
        
        left +=1
        right -= 1
    
    # palindrome if string empty, one character or all corresponding char match
    return True
    
    
#%% test

test = "A man, a plan, a canal: Panama"
print(isPalindrome(test))

test = "race a car"
print(isPalindrome(test))

test = ""
print(isPalindrome(test))