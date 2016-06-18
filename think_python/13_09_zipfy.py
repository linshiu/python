import string
import random


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
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


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency."""
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

import math

def zipfy_list(t):
    f,w= [list(i) for i in zip(*t)]
    r = range(1,len(t)+1)
    log_r = map(math.log,r)
    log_f = [math.log(i) for i in f]
    
    return log_r,log_f 


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)


    t = most_common(hist)
    log_r,log_f =zipfy_list(t)
