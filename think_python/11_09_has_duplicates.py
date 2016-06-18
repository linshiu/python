'''
If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates.'''

def has_duplicates0(t):
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def has_duplicates1(t):
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    d = {}
    
    for i in t:
        d[i] = d.get(i,0) + 1
        if d[i] > 1:
            return True
    return False


def has_duplicates(t):
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    d = {}
    
    for i in t:
        if i in d:
            return True
        d[i]= True
    return False

print has_duplicates('hello')
print has_duplicates('hel')
