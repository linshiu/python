'''Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list'''

'''Modify print_hist to print the keys and their values in alphabetical order.'''

def print_hist(h):
    
    k = h.keys()
    k.sort()
    for c in k:
        print c,h[c]

h = {'b': 2, 'a':1, 'c': 3}
print_hist(h)
