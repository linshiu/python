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


import random

def choose_from_hist(h):
    total = float(sum(h.values()))
    cum_sum = 0
    p = random.random()
    
    for k,v in h.items():
         cum_sum += v/total
         if p < cum_sum:
             return k

    

t = ['a', 'a', 'b']
hist = histogram(t)
print hist

total = 0
counter ={}
for i in range(100):
    res = choose_from_hist(hist)
  
    counter[res] = counter.get(res,0) + 1
 
    total += 1

for i in counter:
    counter[i] = counter[i]/float(total)

print counter
