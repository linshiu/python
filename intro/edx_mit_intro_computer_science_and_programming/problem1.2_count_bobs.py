# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Problem 1.2 - Counting bobs
Python 2.7

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of times bob occurs is: 2


For problems such as these, do not include raw_input statements or 
define the variable s in any way. Our automated testing will provide 
a value of s for you - so the code you submit in the following box should 
assume s is already defined. If you are confused by this instruction,
please review L4 Problems 10 and 11 before you begin this problem set
"""

# script
def countTarget(s, target): 
    
    i = 0
    count = 0
    
    # iterate until last possible first character of target
    while i <= len(s) - len(target):
        if s[i:i+len(target)] == target:
            count+=1
        i+=1
            
    output = "Number of times {0} occurs is: {1}".format(target, count)
    
    # output
    print(output)

# test
s = 'azcbobobegghakl'
t = 'bob'
countTarget(s, t)

# other option with list comprehension
print (len([i for i in range(len(s)) if s.startswith(t, i)]))