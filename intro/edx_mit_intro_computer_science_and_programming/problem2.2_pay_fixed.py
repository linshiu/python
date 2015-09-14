# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Problem 2.1 - Pay Minimum
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
        balance = round(unpaid + annualInterestRate/12.0*unpaid, 2)
    return balance
        
        
def payFixed(balance, annualInterestRate):
    """ Find the minimum monthly payment in increments of $10
        to pay off all balance at end of 1 year
    
    Args:
        balance (numeric): the outstanding balance on the credit card
        annualInterestRate (float): annual interest rate as a decimal
    
    Returns:
        float: Lowest Payment amount
    
    
    """
    
    # start with montly payments of 10
    monthlyFixedPayment = 10
    
    # iterate until the final balance is all paid
    while computeFinalBalance(balance, annualInterestRate, monthlyFixedPayment) > 0:
        
        monthlyFixedPayment += 10
    
    print("Lowest Payment: {0}".format(monthlyFixedPayment))

#%% Test 1

balance = 3329
annualInterestRate = 0.2

payFixed(balance, annualInterestRate)

#%% Test 2

balance = 4773
annualInterestRate = 0.2

payFixed(balance, annualInterestRate)