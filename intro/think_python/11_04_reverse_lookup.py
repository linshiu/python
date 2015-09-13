'''
Modify reverse_lookup so that it builds and returns a list of all keys
that map to v, or an empty list if there are none.'''

def reverse_lookup0(d,v):
    for k in d:
        if v == d[k]:
            return k
    raise ValueError

def reverse_lookup(d,v):
    mapped_keys = []
    for k in d:
        if v == d[k]:
            mapped_keys.append(k)
    return mapped_keys


test = {'a':1,'b':2,'c':3,'d':2}

print reverse_lookup(test,2)
print reverse_lookup(test,1)
print reverse_lookup(test,0)
