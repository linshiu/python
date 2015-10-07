
import string
import random


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    t =[]
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist,t)
    return hist,t


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist,t):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1
        # update list
        t.append(word)


def create_markov(t,n=2):
    '''Create a dictionary where key is a tuple of words that form
    a prefix, and value is a list with possible suffixes.
    t = list of words in order of the text
    n = prefix length'''

    markov = {}
    for i in range(len(t)-n):
        prefix = tuple(t[i:i+n])    
        suffix = t[i+n]
        markov.setdefault(prefix,[]).append(suffix)

    return markov

def create_random_sentence(m,n=2):
    '''Create random sentence based on markov dictionary m
    and number of prefixes n'''
    
    sentence = ''

    prefix = random.choice(m.keys())
    N = len(prefix)
    suffix = random.choice(m[prefix])
    sentence = sentence + ' ' + ' '.join(prefix) + ' ' + suffix
    
    for i in range(n-1):
        prefix = prefix[-(N-1)::] + (suffix,)

        # can get an error if the last word of list is the suffix, because
        # when combined to be a prefix, no key exists
        try:
            suffix = random.choice(m[prefix])
        except KeyError:
            prefix = random.choice(m.keys())
            suffix = random.choice(m[prefix])
            
        sentence = sentence + ' ' + suffix
            
    return sentence

if __name__ == '__main__':

    import random
    hist1,t1 = process_file('emma.txt', skip_header=True)
    hist2,t2 = process_file('book.txt', skip_header=True)
    t = t1 + t2
    
    m = create_markov(t,10)
    s = create_random_sentence(m,50)

    print s
