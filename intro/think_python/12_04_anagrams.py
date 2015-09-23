
def make_anagram_list(filename):
    """creates a list of anagrams
    input = file with words
    output = dictionary of anagrams with key = set of letters sorted
    """

    # key = set of letters sorted, value = list of words
    d = {}
    delimiter = ''
    
    fin = open(filename)

    # loop to create dictionary with anagrams
    for line in fin:

        word = line.strip()

        # create key
        word_sorted = list(word)
        word_sorted.sort()
        word_sorted = delimiter.join(word_sorted)
        
        # add word to the list for that key
        d.setdefault(word_sorted,[]).append(word)

    # delete keys with no anagrams and sort by frequency

    t = []
    for v in d.values():
        if len(v)> 1:
            t.append((len(v),v))

    t.sort(reverse=True)

    anagram_list = []

    for freq, word_list in t:
        anagram_list.append(word_list)
        
    return anagram_list

if __name__ == '__main__':

    anagram_list = make_anagram_list('words.txt')

    print "Number of words with anagrams: " + str(len(anagram_list))

    i=0

    print "Top 10: "

    for a in anagram_list:
        print a
        
        i+=1

        if i == 10:
            break

    # set of 8 letter words most anagrams

    max_n = 0
    t = []
    
    for a in anagram_list:
        
        if len(a[0]) == 8:

           max_n = max(len(a),max_n)

           if len(a) == max_n:
               t.append(a)
           elif len(a) > max_n:
               t = []
               t.append(a)

    print "set of 8 letter words with most anagrams: "
    letters = list(t[0][0])
    letters.sort()
    print letters
    print t
            
