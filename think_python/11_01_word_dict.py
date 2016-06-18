'''
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary'''
import time
from bisect import bisect_left

def make_word_list():
    word_list = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list[word]=word
    return word_list

def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

word_list = make_word_list()
vals = word_list.values()

start = time.clock()
print 'zebra' in word_list
end = time.clock()
print end-start

start = time.clock()
print 'zebra' in vals
end = time.clock()
print end-start

vals.sort()

start = time.clock()
print 'zebra' in vals
end = time.clock()
print end-start

start = time.clock()
print bisect_left(vals,'zebra')
end = time.clock()
print end-start

print vals[-1]
print len(vals)
print word_list['zebra']


