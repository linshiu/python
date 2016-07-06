# -*- coding: utf-8 -*-
"""
Leetcode 155 - Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

#%% Solution 1
# Time: O(n)
# Space: O(n)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.minStack = []
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.stack.append(x)
 
        # update min
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
            

    def pop(self):
        """
        :rtype: void
        """
        if self.stack and self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        if self.stack:
            return self.stack[-1]
        
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        
        else:
            return None
        
        

#%% Solution 2 ################################################################
# Time: O(n)
# Space: O(1)

class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.min = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min:
            self.min = x
        
        # update min
        elif x < self.min:
            self.min = x
        
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            
            popped = self.stack.pop()
            
            # update min only if removed a min
            if popped == self.min:
                self.updateMin()  

    def top(self):
        """
        :rtype: int
        """
        
        if self.stack:
            return self.stack[-1]
        
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        
        
    def updateMin(self):
        
        if self.stack:
            self.min = self.stack[0]
            for i in range(1,len(self.stack)):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]
        else:
            self.min = None
                
            
    

#%% Test #####################################################################


if __name__ == "__main__":
    
    # Your MinStack object will be instantiated and called as such:
    
    minStack = MinStack()
    minStack.push(-2)
    minStack.getMin()   # Returns  -2
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()   # Returns -3.
    minStack.pop()
    minStack.top()    # Returns 0.
    minStack.getMin()   # Returns -2.
    minStack.pop()
    minStack.pop()
    minStack.pop()
    minStack.getMin()
