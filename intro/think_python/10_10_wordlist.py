
'''
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?'''

import time

def create_list1():
    
    start = time.clock()
    fin = open('words.txt')
    new = []
    
    for line in fin:
        word = line.strip()
        new.append(word)    

    end = time.clock()

    print end-start

    return new

t1 = create_list1()
print t1[0]

def create_list2():
    
    start = time.clock()
    fin = open('words.txt')
    new = []
    
    for line in fin:
        word = line.strip()
        new = new + [word]    

    end = time.clock()

    print end-start

    return new

t2 = create_list2()
print t2[0]
