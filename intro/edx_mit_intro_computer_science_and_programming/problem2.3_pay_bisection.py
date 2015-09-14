# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Problem 2.1 - Pay Bisection
Python 2.7

"""

#%% Function

def computeFinalBalance(balance, annualInterestRate, monthlyFixedPayment):
    """ Computes the balance after 1 yar of fixed monthly payments
    
    Args:
        balance (numeric): the outstanding balance on the credit card
        annualInterestRate (float): annual interest rate as a decimal
        monthlyFixedPayment (numeric): monthly fiexed payment
    
    Returns:
        float: final balance after 1 year 
        
    """
    for month in range(1,12+1):
        payment = monthlyFixedPayment
        unpaid = balance - payment
        balance = unpaid + annualInterestRate/12.0*unpaid
    return balance
        

def payBisection(balance, annualInterestRate):
    """ Find the minimum monthly payment to pay off all balance at end of 1 year
    
    Use bisection method to speed up calculation
    
    Args:
        balance (numeric): the outstanding balance on the credit card
        annualInterestRate (float): annual interest rate as a decimal
    
    Returns:
        None: print Lowest Payment amount
    
    """
    
    low = balance / 12.0
    high = (balance * (1 +annualInterestRate/12 )**12) / 12.0
    
    epsilon = 0.01
    guess = (low + high)/2.0
    target = 0
    
    finalBalance = computeFinalBalance(balance, annualInterestRate, guess)
    
    while abs(finalBalance - target) > epsilon:
        
        if finalBalance < 0:
            high = guess
        else:
            low = guess
        
        guess = (low + high)/2.0
        finalBalance = computeFinalBalance(balance, annualInterestRate, guess)
        
    
    print("Lowest Payment: {0}".format(round(guess,2)))
    

#%% Test 1

balance = 320000
annualInterestRate = 0.2

payBisection(balance, annualInterestRate)

#%% Test 2

balance = 999999
annualInterestRate = 0.18

payBisection(balance, annualInterestRate)