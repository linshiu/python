# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:04:55 2016

@author: Steven
"""

from datastructures import Stack


def checkBalance(s, d = {'(':')', '[':']', '{': '}', '<':'>'}):
    ''' check balanced symbols
    
    Args:
        s (str): string of parenthesis
        d (dict): dictionary key: open symbol, value = close symbol
        
    Returns:
        boolean: True if balanced, False if not balanced
    
    '''
    
    S = Stack()

    for i in s:
        
        # push if open symbol
        if i in d:
            S.push(i)
        
        # unbalanced if no opening to match closing or mismatch open/close symbols
        elif S.isEmpty() or d[S.pop()] != i:
            return False
        
        # no need because popped in previous statment instead of peeked
        # there is a match in open/close so cancel out by popping
        # else:
           #S.pop()
                
    
    # only if empty (all canceled out) then balanced
    return S.isEmpty()
    

if __name__ == '__main__':
    
    test = ['(())<>','({}())','(()))', '(()})',')()']
    
    for t in test:
        print(checkBalance(t))


