# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L4 PROBLEM 11 - IsVowel2
Python 2.7

Define a function isVowel2(char) that returns True if char is a 
vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. 
You can assume that char is a single letter of any case 
(ie, 'A' and 'a' are both valid).

This function is similar to the previous problem - 
but this time, do use the keyword in. Your function 
should take in a single string and return a boolean.

"""

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    c = char.lower()
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    return c in vowels
    
print (isVowel2("E"))
print (isVowel2('p'))