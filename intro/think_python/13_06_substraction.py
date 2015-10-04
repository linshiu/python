'''
Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times
each word is used.
Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?'''

import string

def read_file(filename):

    word_list = []
    
    fin = open(filename)

    #create table to translate punctuations to spaces
    intab = string.punctuation
    outab = ' '*len(intab)
    trantab = string.maketrans(intab, outab)

    header = True
    
    for line in fin:
        line = line.strip()
        word_list = line.translate(trantab).lower().split()

        '''
        if header:
            if word_list[:3] == '***':
                header = False  
            continue'''
        
        histogram(word_list)
        
    return word_list


hist = {}
def histogram(t):
    for word in t:
        hist[word] = hist.get(word,0) + 1

def histogram_list():
    total = float(sum(hist.values()))
    t = []
    for k,v in hist.items():
        t.append((v/total,k))

    t.sort(reverse=True)

    return t


def print_hist(n):

    print "Total number of diffeent words: " + str(len(t)) + '\nFrequency:'
    for freq,word in t[:n]:
        print word,' '*(20 - len(word)),"{0:.2f}%".format(freq * 100)

        
read_file('book.txt')
t= histogram_list()
print_hist(n=20)


def make_word_dict():
    """Reads the words in words.txt and returns a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

word_dict = make_word_dict()

def not_in_word_list():
    count = 0
    for word in hist:
        if word not in word_dict:
            count+=1
            print word
    print "***Number of words not in dict:" + str(count)
    print "{0:.2f}%".format(float(count)/len(hist) * 100) +" of words in book not in dict"
    print "{0:.2f}%".format(float(count)/len(word_dict) * 100) +" of words in dict used in book"

not_in_word_list()

def substraction(d1,d2):
    s1 = set()
    s2 = set()

    for k in d1:
        s1.add(k)
    for k in d2:
        s2.add(k)

    return s1.difference(s2)

diff = substraction(hist,word_dict)

