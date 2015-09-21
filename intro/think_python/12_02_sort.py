'''
In this example, ties are broken by comparing words, so words with the same length
appear in reverse alphabetical order. For other applications you might want to break ties at random.
Modify this example so that words with the same length appear in random order. Hint:
see the random function in the random module.'''

import random

def sort_by_length(words):

    t =[]
    
    for word in words:
        t.append((len(word),random.random(),word))

    t.sort(reverse=True)

    res = []


    #for length,rnd,word:
    #   res.append(word)

    for i in t:
        res.append(i[-1])

    return res


test = ['boy','si','bit']

print sort_by_length(test)
