# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Lecture 3 - Problem 9 - Bisection
Python 2.7

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? Using 
bisection search, the computer will guess the user's secret number!


"""

low = 0
high = 100
print("Please think of a number between {0} and {1}!".format(low, high))
guess = int( (low+high)/2)
      
# pyhon 3
def promptInput(guess):
    ans = input ( "Is your secret number " + str(guess) + "?\n" +
                  "Enter 'h' to indicate the guess is too high. " + 
                  "Enter 'l' to indicate the guess is too low. " + 
                  "Enter 'c' to indicate I guessed correctly. ")
    return ans
"""
# pyhon 2.7        
def promptInput(guess):
    print("Is your secret number {}?".format(guess))
    ans = raw_input ( "Enter 'h' to indicate the guess is too high. " + 
                      "Enter 'l' to indicate the guess is too low. " + 
                      "Enter 'c' to indicate I guessed correctly. ")
"""    
    
ans = promptInput(guess)
# bisect until find right answer
while ans != 'c':
    
    # too high
    if ans == "h":
        high = guess
        guess = int( (low+high)/2)
        
    # too low
    elif ans == "l":
        low = guess
        guess = int( (low+high)/2)
        
    # incorrect input
    else: 
        print("Sorry, I did not understand your input.")
        
    ans = promptInput(guess)    
                
print ("Game over. Your secret number was: {}".format(guess))
   
    
    