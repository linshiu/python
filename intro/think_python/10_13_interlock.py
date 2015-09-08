# -*- coding: cp1252 -*-
'''
Two words 'interlock' if taking alternating letters from each forms a new
word. For example, 'shoe' and 'cold' interlock to form schooled.'''

'''
Write a program that finds all pairs of words that interlock'''

from bisect import bisect_left


def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
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


def interlock(word_list,word,n=3):
    for i in range(n):
        if not in_bisect(word_list,word[i::n]):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()

    print '****************three-way' 
    for word in word_list:
        if interlock(word_list,word,2):
            print '%(word)s,%(word1)s,%(word2)s' % {'word':word,'word1':word[::2],'word2':word[1::2]}
            
    print '****************three-way'

    for word in word_list:
        if interlock(word_list,word):
            print '%(word)s,%(word1)s,%(word2)s,%(word3)s' % {'word':word,'word1':word[::3],
                                                              'word2':word[1::3],'word3':word[2::3]}
    
    

