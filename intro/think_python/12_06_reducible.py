
def make_word_dict():
    """Reads the words in words.txt and returns a dictionary
    that contains the words as keys."""
    word_dict = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_dict[word]=word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        word_dict[letter] = letter

    return word_dict

def remove_letter(word, index):
    t = list(word)
    del t[index]
    return ''.join(t)


def get_child(word):
    child = []
    for i in range(len(word)):
        new = remove_letter(word,i)
        if new in word_dict:
            child.append(new)
    return child


""" reducible_dict  is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

reducible_dict = dict(zip(['','i','a'],[True for i in range(3)]))

def is_reducible(word):
    """If word is reducible, returns a list of its reducible children.

    Also adds an entry to the reducible_dict dictionary.

    A string is reducible if it has at least one child that is 
    reducible.  The empty string is also reducible.

    word: string
    
    """

    # check known reducible words
    if word in reducible_dict:
        return reducible_dict[word]
    
    children = get_child(word)

    #if no children, is not reducible
    if children == []:
        res = False
        reducible_dict[word] = res
        return res

    # otherwise, loop through children
    # until find at least one children that is reducible
    for child in children:
        res = is_reducible(child)

        if res == True:
            reducible_dict[word] = res
            return res

    # if none of the chidren reducible, then word is not reducible
    reducible_dict[word] = res
    return res

def fill_reducibles_dict():
    for word in word_dict:
        is_reducible(word)

def reducibles_list(d):
    t =[]
    for k,v in d.items():
        if v == True:
            t.append((len(k),k))

    t.sort(reverse=True)

    res = []
    for length,word in t:
        res.append(word)
        
    return res

word_dict = make_word_dict()
fill_reducibles_dict()
t = reducibles_list(reducible_dict)
print t[0:10]


