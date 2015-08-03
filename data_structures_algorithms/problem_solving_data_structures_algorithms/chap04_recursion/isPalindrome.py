# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 4: Recursion
Palindrome

IDE: Spyder, Python 3

Check if word is a palindrome using recursion. 

A string is a palindrome if it is spelled the same both forward
and backward. for example: radar is a palindrome. for bonus points 
palindromes can also be phrases, but you need to remove the spaces 
and punctuation before checking. for example:
madam i’m adam is a palindrome

"""
#%% Function #################################################################
import re

def isPalindrome(string):
    """ Check if string is palindrome
    
    Base: length of string is <=1 (even -> 0, odd -> 1)
    Change state: reduce the string by taking front and rear
    Recursion: Call itself (pass reduced string)
    
    Args:
        string (str): word or phrase to test
        
    Returns:
        boolean: True if palindrome, False otherwise
    
    """
    string = re.sub(r'[\W_]+', '', string).lower()
    
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])

#%% Test #####################################################################
def test():
    stringDic = {"kayak": True,"kayaks": False, "": True, "k": True,
                 "kk": True, "kp": False, "Madam, I'm Adam.": True}
    
    for string,result in stringDic.items():
        assert isPalindrome(string) == result
        
    print("Test: Success")

if __name__ == "__main__":
    test()