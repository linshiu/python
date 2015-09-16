# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L5 PROBLEM 8 - isIn
Python 2.7

We can use the idea of bisection search to determine if a character is in a 
string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're 
looking for (the "test character"). If they are the same, we are done -
 we've found the character we're looking for!

If they're not the same, check if the test character is "
smaller" than the middle character. If so, we need only consider 
the lower half of the string; otherwise, we only consider the 
upper half of the string. (Note that you can compare characters 
using Python's < function.)

Implement the function isIn(char, aStr) which implements the 
above idea recursively to test if char is in aStr. char will be a 
single character and aStr will be a string that is in alphabetical order. 
The function should return a boolean value.

As you design the function, think very carefully about what the base 
cases should be.

"""

#%%

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    # base cases
    if len(aStr) == 0: # this can happen for cases when aStr is odd length
        return False
    
    elif len(aStr) == 1:
        return aStr == char
    
    # recursive cases
    
    mid = int(len(aStr)/2)
    
    if char == aStr[mid]:
        return True
        
    elif char < aStr[mid] :
        return isIn(char, aStr[:mid])
        
    else:
        
        # note that not out of bounds for slicing, so if mid + 1 >  len - 1,
        # the slicing will result in empty string
        # this takes care of case of len(aStr) = 2 and the previous
        # two conditional tests are false
        return isIn(char, aStr[mid+1:])
    

    
#%%
    
isIn('m', 'fgkmtxx')
isIn('m', 'fgkmtx')
isIn('h', 'fgkmtx')