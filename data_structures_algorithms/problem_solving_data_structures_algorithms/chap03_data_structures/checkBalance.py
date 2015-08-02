# -*- coding: utf-8 -*-
"""
Problem Solving with Algorithms and Data Structures, Miller
Chapter 3: Basic Data Structures

IDE: Spyder, Python 3

Check if a string has balanced parenthesis (or more general balanced symbols)

Balanced parentheses means that each opening symbol has a corresponding 
closing symbol and the pairs of parentheses are properly nested. (Miller)

"""
#%% ##### Stack Immplementation ##############################################

#%% My Stack Immplementation

class Stack:
        def __init__(self):
            self.items =[]
            
        def isEmpty(self):
            return self.items == []
            
        def size(self):
            return len(self.items)
            
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            return self.items.pop()
            
        def peek(self):
            return self.items[len(self.items)-1]       

#%% Test Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

#%% ##### Balanced Parenthesis ##############################################
#%% My Function

def checkBalance(mystring, openSym = "(", closeSym = ")" ):
    """ Check if the symbol in a string is balanced
    
    Steps
    1) start from beginnning and add "(" to stack
    2) when a ")" is found , remove corresponding "(" from stack (last in stack)
    3) stack should be empty after iterating the string
    
    Args:
        mystring (str): string of characters
        openSym (Optional[str]): open symbol. Defaults to "("
        closeSymb (Optional[str]): close symbol: Defaults to ")"
        
    Returns:
        boolean: True if balanced, False otherwise
    
    """
    
    s = Stack()
    
    for ch in mystring:
        
        if ch == openSym:
            s.push(ch)
            
        elif ch == closeSym:
            
            # there has to be a an open before for a closing
            if s.isEmpty():
                return False
                
            s.pop()
    
    return s.isEmpty()
            
#%%  Test      
test1 = "(12+15)*(24-2)*(10+(2-4))"
test2 = "(12/24))"
test3 = ")test4()"
test4 = "jj<j>"

print (checkBalance(test1))
print (checkBalance(test2))
print (checkBalance(test3))
print (checkBalance(test4,"<",">"))

#%% ##### General Balanced Parenthesis #######################################
#%% My Function

def checkBalance2(mystring, symbolDic ):
    """ Check if the symbol in a string is balanced
    
    Steps
    1) start from beginnning and add "(" to stack
    2) when a ")" is found , remove corresponding "(" from stack (last in stack)
    3) stack should be empty after iterating the string
    
    Args:
        mystring (str): string of characters
        symbolDic (dict): mapping open to close symbols
        
    Returns:
        boolean: True if balance, False otherwise
    
    """
    
    s = Stack()
    
    for ch in mystring:
        
        if ch in symbolDic:
            s.push(ch)
            
        elif ch in symbolDic.values():
            
            # there has to be a an open of the same type before for a closing
            if s.isEmpty() or symbolDic[s.pop()] != ch :
                return False
    
    return s.isEmpty()


# open to close mapping

#%% Test
symbolDic = {"(": ")", "{": "}","[":"]" }

print(checkBalance2('{{([][])}()}', symbolDic))
print(checkBalance2('[{()]', symbolDic))
