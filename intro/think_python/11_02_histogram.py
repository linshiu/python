def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

print histogram('hello')

'''
Use get to write histogram more concisely.
You should be able to eliminate the if statement'''

def histogram(s):
    d = dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

print histogram('hello')
