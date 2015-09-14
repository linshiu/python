# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
Problem 2.1 - Pay Minimum
Python 2.7

"""

#%% Function

def payMinimum(balance, annualInterestRate, monthlyPaymentRate ):
    """ Prints the monthly balance and payment for 1 year based on the 
        minimum monthly payment each month
        
    Args:
        balance (numeric): the outstanding balance on the credit card
        annualInterestRate (float): annual interest rate as a decimal
        monthlyPaymentRate (float): minimum monthly payment rate as a decimal
        
    Returns:
        None: prints monthly results and final balance after 1 year
        
    """

    totalPaid = 0
    
    for month in range(1,12+1):
    
        # monthly payment, based on the previous month’s balance
        payment = round(balance*monthlyPaymentRate, 2)
        
        # Update the outstanding balance by removing the payment, then charging interest on the result
        unpaid = balance - payment
        balance = round(unpaid + annualInterestRate/12.0*unpaid, 2)
        
        # Keep track of the total amount of paid over all the past months so far
        totalPaid += payment
        
        # Output the month, the minimum monthly payment and the remaining balance
        output = ("Month: {0}\n" 
                  "Minimum monthly payment: {1}\n" 
                  "Remaining balance: {2}".format(month, payment, balance))
                  
        print(output)
        
    # Print out the result statement with the total amount paid and the remaining balance
    print ("Total paid: {0}\n"
           "Remaining balance: {1}".format(round(totalPaid,2), balance))

#%% Test 1

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

payMinimum(balance, annualInterestRate, monthlyPaymentRate )

#%% Test 2

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

payMinimum(balance, annualInterestRate, monthlyPaymentRate )