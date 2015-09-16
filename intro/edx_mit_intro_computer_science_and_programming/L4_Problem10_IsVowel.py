# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L4 PROBLEM 10 - IsVowel
Python 2.7

Define a function isVowel(char) that returns True if char 
is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. 
You can assume that char is a single letter of any case 
(ie, 'A' and 'a' are both valid).

Do not use the keyword in. Your function should take in a 
single string and return a boolean.


"""

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    c = char.lower()
    
    return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')
    
print (isVowel("E"))
print (isVowel('p'))