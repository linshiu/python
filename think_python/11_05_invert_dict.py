'''
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict'''

def invert_dict0(d):
    inverse = dict()
    for k in d:
        v = d[k]
        if v not in inverse:
            inverse[v] = [k]
        else:
            inverse[v].append(k)
    return inverse

test = {'a':1, 'b':2,'c':1}

print invert_dict0(test)

def invert_dict(d):
    inverse = dict()
    for k,v in d.items():
        inverse.setdefault(v,[]).append(k)
    return inverse

test = {'a':1, 'b':2,'c':1}

print invert_dict(test)
