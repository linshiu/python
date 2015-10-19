# -*- coding: utf-8 -*-
"""
edX - MIT - Introduction to Computer Science and Programming
L11 PROBLEM 4 - factorial
Python 2.7

"""
#%%
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self,other):
        
        assert type(other) == type(self)
        
        return self.x == other.getX() and self.y == other.getY()
        
    def __repr__(self):
        
        return "Coordinate({x}, {y})".format(x = self.x, y = self.y)
        
        

#%%

p1 = Coordinate(1,2)
p2 = Coordinate(1,2)
p3 = Coordinate(1,3)
# Test equality

print(p1==p2)
print(p1==p3)




print(p1)
p1

eval(repr(p1)) == p1