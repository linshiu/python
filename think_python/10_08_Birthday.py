from __future__ import division  # single slash (/) for true (non-truncating) division.
                                 # (The // operator is used for truncating division.)

'''
Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.'''

def has_duplicates(t):
    t_sorted = t[:]
    t_sorted.sort()

    if len(t_sorted) <= 1:
        return False

    if t_sorted[0] == t_sorted[1]:
        return True

    return has_duplicates(t[1:])

import random

def integer_list(start,end,size):
    i = 0
    t = []
    while i < size:
        t.append(random.randint(start,end))
        i+=1
    return t

def check_birthday(n):
    i = 0
    count = 0
    while i < n:
        if has_duplicates(integer_list(1,365,23)):
            count+=1
        i+=1
    print count
    print count/n

check_birthday(10000)
