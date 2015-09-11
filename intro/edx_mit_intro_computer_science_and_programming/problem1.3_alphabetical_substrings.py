# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Problem 1.2 - Counting bobs
Python 2.7

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or 
define the variable s in any way. Our automated testing will provide 
a value of s for you - so the code you submit in the following box should 
assume s is already defined. If you are confused by this instruction,
please review L4 Problems 10 and 11 before you begin this problem set
"""

# script
def findLongestSubstr(s): 
    
    # initialize
    subStr = s[0]
    longest = subStr
    i = 1
    
    while i < len(s):
        
        # keep appending if last char of current substring is less than char in s
        if subStr[-1] <= s[i]:
            subStr += s[i]
             
        # reset and updte
        else:
            if len(subStr) > len(longest):
                longest = subStr      # update longest
                
            subStr = s[i]             # reset regardless if longest updated
        
        i+=1
        
    # update max in case entire string s is alphabetically ordered
    if len(subStr) > len(longest):
        longest = subStr
               
    output = "Longest substring in alphabetical order is: {}".format(longest)
    
    # output
    print(output)

# test
s = 'azcbobobegghakl'
findLongestSubstr(s)

s = 'abcbcd'
findLongestSubstr(s)

s = 'bxlbqbvycjhp'
findLongestSubstr(s)

s = 'abcdefghijklmnopqrstuvwxyz'
findLongestSubstr(s)
