# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 1: Intro
Fraction class example

Python 3.0
IDE: Sypder

Immplement a class for fractions
"""
#%% My Function and Classes

def gcd(m,n):
    """ Euclid’s Algorithm states that the greatest common divisor of two 
    integers m and n is n if n divides m evenly. However, if n does not
    divide m evenly, then the answer is the greatest common divisor of n 
    and the remainder of m divided by n (Miller)

    Args:
        m (int): number
        n (int): number
    Returns:
        int: greatest common divisor
    """
    while m%n != 0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
        
    return n
    
class Fraction:
    
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    
    def show (self):
        print (str(self.top) + "/" + str(self.bottom))
        
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)
        
    def __repr__(self):
        return str(self.top) + "/" + str(self.bottom)
        
    def __add__ (self, otherfraction):
        den = self.bottom*otherfraction.bottom
        num = self.top*otherfraction.bottom + self.bottom*otherfraction.top
        common = gcd(num,den)
        return Fraction(num//common,den//common)
        
    def __eq__ (self, otherfraction):
        firstnum = self.top*otherfraction.bottom
        secondnum = self.bottom * otherfraction.top
      
        return firstnum == secondnum
      
      


#%% Test

myfraction = Fraction(3,5)
myfraction
print(myfraction)

f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)

x = Fraction(1,2)
y = Fraction(4,8)
print(x+y)
print(x == y)

print(gcd(20,10))