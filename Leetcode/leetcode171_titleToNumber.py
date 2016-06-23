# -*- coding: utf-8 -*-
"""
Leetcode 171 - Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
    
"""

#%% method 1

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A -> 1
        base = ord("A") - 1        
        
        number = 0
        for index,letter in enumerate(reversed(s)):
            number += (ord(letter) - base)*26**index
        
        return number
        
#%% method 2
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A -> 1
        base = ord("A") - 1        
        return sum([(ord(letter)-base)*26**index for (index,letter) in enumerate(reversed(s))])
        
#%% Test
        
if __name__ == "__main__":
    test = Solution()
    ls = ["A", "Z", "AA", "ZZ", "AAA", "BAA", "CAA"]
    for element in ls:
        print(element + "-->" + str(test.titleToNumber(element)))


