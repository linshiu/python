''''Write a function called is_sorted that takes a list as a parameter
and returns True if the list is sorted in ascending order and False
otherwise. You can assume (as a precondition) that the elements of
the list can be compared with the relational operators <, >, etc.'''

def is_sorted(t):
    t_sorted = t[:]
    t_sorted.sort()
    return t == t_sorted

test1 = ['1','2','3']
test2 = ['3','1','2']
test3 = ['a','b','c']
test4 = ['a','c','b']

print is_sorted(test1)
print is_sorted(test2)
print is_sorted(test3)
print is_sorted(test4)

def is_sorted2(t):

    i=0

    while i < len(t)-1:

        if t[i] > t[i+1]:
            return False

        i+=1

    return True

print is_sorted2(test1)
print is_sorted2(test2)
print is_sorted2(test3)
print is_sorted2(test4)

def is_sorted3(t):

    if len(t)<=1:
        return True

    if t[0] > t[1]:
        return False

    return is_sorted3(t[1:])

    

    return True

print is_sorted3(test1)
print is_sorted3(test2)
print is_sorted3(test3)
print is_sorted3(test4)

