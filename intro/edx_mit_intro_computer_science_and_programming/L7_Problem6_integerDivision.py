# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L7 PROBLEM 6 - biggest
Python 2.7

"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count