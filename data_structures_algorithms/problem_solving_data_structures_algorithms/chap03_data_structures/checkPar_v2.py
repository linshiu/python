# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:04:55 2016

@author: Steven
"""

from datastructures import Stack


def checkPar(s):
    ''' check balanced parenthesis
    
    Args:
        s (str): string of parenthesis
    
    '''
    
    S = Stack()

    for i in s:
        
        if S.isEmpty():
            
            if i == '(':
                S.push(i)
                
            # imbalance
            else:
                return False
        
        else:
            if S.peek() == i:
                S.push(i)
                
            # cancel out parenthesis
            else:
                S.pop()
    
    # only if empty (all canceled out) then balanced
    return S.isEmpty()
    

if __name__ == '__main__':
    
    test = ['(())','(()())','(()))', '(()()))',')()']
    
    for t in test:
        print(checkPar(t))


