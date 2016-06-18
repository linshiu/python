def middle(t):
    return t[1:-1]

print middle([1,2,3,4])

def middle2(t):

    res = []
    i = 1
    while i <= len(t)- 2:
        res.append(t[i])
        i+=1

    return res

print middle2([1,2,3,4])
