# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L7 PROBLEM 8 - factorial
Python 2.7

"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
        
#%% test
f(3)
f(1)
f(0)