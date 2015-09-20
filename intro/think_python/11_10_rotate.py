'''
ROT13 is a weak form of encryption that involves 'rotating' each letter in a word
by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
beginning if necessary, so 'A' shifted by 3 is 'D' and 'Z' shifted by 1 is 'A'.
Write a function called rotate_word that takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string 'rotated' by the given amount.
For example, 'cheer' rotated by 7 is 'jolly' and 'melon' rotated by -10 is 'cubed'.
You might want to use the built-in functions ord, which converts a character to a numeric code,
and chr, which converts numeric codes to characters.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily
offended, find and decode some of them.


Two words are 'rotate pairs' if you can rotate one of them and get the other (see
rotate_word in Exercise 8.12).
Write a program that reads a wordlist and finds all the rotate pairs.

'''

def rotate_letter(letter,n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    return chr(((ord(letter) - start) + n )%26 + start)

def rotate_word(word,n):
    rotated =''
    for letter in word:
        rotated+=rotate_letter(letter,n)
    return rotated


def rotate_pairs(word, word_dict):

    for i in range(1,14):
        rotated = rotate_word(word,i)      
        if rotated in word_dict:
            print word,i, rotated


word_dict = {}        

fin = open("words.txt")

for line in fin:
    word = line.strip()
    word_dict[word]=word

for word in word_dict:
    rotate_pairs(word,word_dict)


         
print rotate_letter('a',-1)
print rotate_word('Abc',1)
