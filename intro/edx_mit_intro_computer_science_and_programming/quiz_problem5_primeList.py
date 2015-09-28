# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Quiz - Problem 5
Python 2.7

Write a Python function that creates and returns a list of prime numbers
between 2 and N, inclusive, sorted in increasing order. A prime number 
is a number that is divisible only by 1 and itself. This function takes
in an integer and returns a list of integers.

http://www.wikihow.com/Check-if-a-Number-Is-Prime

"""

#%% Function
import math

def primesList(N):
    ''' Returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order
    
    Args:
        N: an integer
    
    Returns:
        list: Returns a list of prime numbers
        
    '''
 
    primeL = [2]
    
    # find primes up to N
    for n in range(3,N+1):

        # for a number x, it is prime if all prime numbers >=2 up to sqrt(x)
        # give remainder different than zero
        
        isPrime = True
        sqrt = math.sqrt(n)
        j = 0 # index of current primeList
    
        while j < len(primeL) and primeL[j] <= sqrt and isPrime:
            
            if n % primeL[j] == 0:
                isPrime = False
            
            j+=1
               
        if isPrime:
            primeL.append(n)
            
    return primeL
        
#%% Test
        
print(primesList(24)) # [2, 3, 5, 7, 11, 13, 17, 19, 23]