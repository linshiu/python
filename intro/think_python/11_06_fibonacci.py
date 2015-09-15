import time

def fibonacci0(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci0(n-1) + fibonacci0(n-2)

known ={0:0, 1:1}

def fibonacci1(n):
    if n in known:
        return known[n]

    res = fibonacci1(n-1) + fibonacci1(n-2)
    known[n] = res
    return res

for n in range(32,33):
    t1 = time.clock()
    fibonacci0(n)
    t2= time.clock()
    
    fibonacci1(n)
    t3 = time.clock()

    print n,t2-t1, t3-t2

    

    
    
