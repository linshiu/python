# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Brad Miller
Chapter 4: Recursion

IDE: Spyder, Python 3

Reverse a list

"""
#%% Function #################################################################
def reverseList(ls):
    """ Reverse a list
    
    base: 
    
    Args:
        ls (list): list to reverse
    
    Regturns:
        list: reversed list
    
    """

    if len(ls) <= 1:
        return ls

    else:
        return reverseList(ls[1:]) + [ls[0]]


#%%  Testl #################################################################

def test():
    testList = [0,1,2,3,4]
   
    rev = reverseList(testList) 
    testList.reverse()
    assert rev == testList
    
    print("Test: Success")


if __name__ == "__main__":

    test()