# -*- coding: utf-8 -*-
"""

edX - MIT - Introduction to Computer Science and Programming
L12 PROBLEM 4 - Primes
Python 2.7
Write a generator, genPrimes, that returns the sequence of prime numbers
 on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Hints
Ideas about the problem
Have the generator keep a list of the primes it's generated. 
A candidate number x is prime if (x % p) != 0 for all earlier primes p.

"""

def genPrimes():
    
    prime_list = []
    x = 2
    
    while True:
          
        prime = True
        i = 0
      
        while prime and i < len(prime_list):
            
            if (x % prime_list[i]) ==  0:
                prime = False
            
            i+=1
        
        if prime:
            prime_list.append(x)
            yield x
        
        x += 1
    
    
#%%

primes = genPrimes()
maxN = 100
for n in primes:
    print n
    if n > maxN:
        break;