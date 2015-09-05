'''
Two words are anagrams if you can rearrange
the letters from one to spell the other.
Write a function called is_anagram that takes two
strings and returns True if they are anagrams'''

def is_anagram(word1,word2):
    
    t1 = list(word1)
    t2 = list(word2)

    t1.sort()
    t2.sort()

    return t1 == t2


word1 = 'anfield'
word2 = 'delfina'

print is_anagram(word1,word2)
print is_anagram('jfe','mik')
