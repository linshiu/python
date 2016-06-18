'''
Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
Hint: The string module provides strings named whitespace, which contains space, tab, newline,
etc., and punctuation which contains the punctuation characters.'''

import string

def read_file(filename):

    word_list = []
    
    fin = open(filename)

    #create table to translate punctuations to spaces
    intab = string.punctuation
    outab = ' '*len(intab)
    trantab = string.maketrans(intab, outab)
    
    for line in fin:
        line = line.strip()
        line = line.translate(trantab).lower().split()
        word_list.extend(line)
        
    return word_list

print read_file('test.txt')




