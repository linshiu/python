# -*- coding: utf-8 -*-
"""
Monkeys example

@author: slin
"""

""" Example 1
You may have heard of the infinite monkey theorem? 
The theorem states that a monkey hitting keys at random 
on a typewriter keyboard for an infinite amount of time 
will almost surely type a given text, such as the complete 
works of William Shakespeare. Well, suppose we replace a 
monkey with a Python function. How long do you think it would take
for a Python function to generate just one sentence of Shakespeare? 
The sentence we’ll shoot for is: "methinks it is like a weasel"

You’re not going to want to run this one in the browser, so fire up your 
favorite Python IDE. The way we’ll simulate this is to write a function 
that generates a string that is 27 characters long by choosing random 
letters from the 26 letters in the alphabet plus the space. We’ll write 
another function that will score each generated string by comparing the 
randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 
100% of the letters are correct we are done. If the letters are not 
correct then we will generate a whole new string.To make it easier to 
follow your program’s progress this third function should print out the 
best string generated so far and its score every 1000 tries.

"""

""" Example 2
See if you can improve upon the program by keeping 
letters that are correct and only modifying one character in the best 
string so far. This is a type of algorithm in the class of ‘hill climbing’ 
algorithms, that is we only keep the result if it is better than the previous one.
"""

#%%
import random
import time

def generateRandom(n):
    """" Generates a random string of length from alphabet plus space
    
    Args:
        n (int): length of string
    
    Return:
        str: random string
    
    """
    characters = "".join([chr(i) for i in range(97,97+26)]) + " "
    rstr = "".join([characters[random.randint(0, len(characters)-1)] for i in range(n)])
    return rstr
    
def scoreRandom(targetS,randomS):
    """ pct of corresponding (same position) matching charaters 
    
    Args:
        targetS (str): target string
        randomS (str): random string
        
    Return:
        float: percent of correct positional match
    
    """
    
    return sum([t==r for (t,r) in zip(targetS,randomS) ])/len(targetS)
    

def repeatRandom(targetS):
    """ Find out tries and time it takes to generate target string
    If the letters are not correct then we will generate a whole new 
    string.To make it easier to follow your program’s progress
    print out the best string generated so far and its score every 1000 tries.
    
    Args:
        targetS (str): target string
    
    Return:
        None

    """
    initialTime = time.time()
    elapsedTime = 0
    totalIter = 0
    match = False
    n = len(targetS)
    bestScore = 0
    bestRandom = ""
    
    while not match:
        
        totalIter += 1
        
        randomS = generateRandom(n)
        score = scoreRandom(targetS, randomS)
        
        if score > bestScore:
            bestScore = score
            bestRandom = randomS
        
        if score ==1:
            match = True
        
        if totalIter % 1000 == 0:
            elapsedTime = time.time() - initialTime
            msg = "Iterations: {i}, Time Elapsed: {t}, Best Score: {s}, Best String: {st} ".format(i = totalIter, 
                                        t = elapsedTime,
                                        s = bestScore,
                                        st = bestRandom)
            print (msg)
    
    elapsedTime = time.time() - initialTime
    
    print (randomS)
    print (score)
    print (totalIter)
    print (elapsedTime)
    
#%% Test
    
s = "methinks it is like a weasel"
s= "hello"
len(s)

repeatRandom(s)

# takes too long

#%% Hill Climbing
