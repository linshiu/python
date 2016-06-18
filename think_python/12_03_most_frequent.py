'''
Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http: //
en. wikipedia. org/ wiki/ Letter_ frequencies . Solution: http: // thinkpython. com/
code/ most_ frequent. py .'''

def histogram(s):
    hist = {}
    for i in s:
        hist[i] = hist.get(i,0)+1
    return hist
        

def most_frequent(s):
    hist = histogram(s)
    t = []
    for k,freq in hist.items():
        t.append((freq,k))

    t.sort(reverse=True)

    res =[]

    for freq,k in t:
        res.append(k)

    return res

        
test = 'hello'
t = most_frequent(test)

for i in t:
    print i
    
