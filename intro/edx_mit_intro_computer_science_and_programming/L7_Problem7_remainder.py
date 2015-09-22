# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L7 PROBLEM 7 - rem
Python 2.7

"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
#%% test
print(rem(2, 5))
print(rem(5, 5))
print(rem(7, 5))