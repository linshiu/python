# -*- coding: utf-8 -*-
"""
Problem Solving with Data Structures and Algorithms, Brad Miller
Chapter 2 - Analysis
Anagram

IDE: Spyder, Python 3

A good example problem for showing algorithms with different orders of 
magnitude is the classic anagram detection problem for strings. One string
is an anagram of another if the second is simply a rearrangement of the first. 
For example, 'heart' and 'earth' are anagrams. The strings 'python' and 
'typhon' are anagrams as well. For the sake of simplicity, we will assume
 that the two strings in question are of equal length and that they are
 made up of symbols from the set of 26 lowercase alphabetic characters. 
 Our goal is to write a boolean function that will take two strings and
 return whether they are anagrams (Miller)
 
"""
#%% My Solution
import matplotlib.pyplot as plt
import random
import time

def getFrequency(word):
    """ Get frequency of letter in word
    
    Args:
        word (string): string of word
        
    Returns:
        dic: {key: letter from alphabet, value: count in word}
        
    """
    alphabet = [chr(i) for i in range(97,97+26)]
    freqDic = {key: value for (key, value) in zip(alphabet,[0]*len(alphabet))}
    for letter in word:
        freqDic[letter]+=1
    return freqDic
    
def checkAnagram(word1,word2):
    """ Check if two words are anagrams
    
    Args:
        word1 (string): first word
        word2 (string): second word
    
    Returns:
        boolean: True if anagrams, False otherwise
        
    """
    
    alphabet = [chr(i) for i in range(97,97+26)]
    
    if len(word1)!=len(word2):
        return False
    
    word1Dic = getFrequency(word1)
    word2Dic = getFrequency(word2)
    
    for letter in alphabet:
        if word1Dic[letter] != word2Dic[letter]:
            return False
    
    return True


#%% test
print(checkAnagram('apple','pleap'))
