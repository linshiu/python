def chop(t):
    del t[0]
    del t[-1]

x = [1,2,3,4]

chop(x)
print x
