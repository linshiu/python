import tpy_12_04_anagrams as ana

# a metathesis pair have to be anagrams because they use the same letters
def swap(word,i,j):
    ''' swap letters in word'''
    swapped = list(word)
    swapped[i],swapped[j] = swapped[j],swapped[i]
    swapped = ''.join(swapped)

    return swapped


def metathesis_word(word, a_list, m_list):
    ''' appends metathesis pairs

    '''

    count = 0
    # swap all possible combination (order doesn't matter)
    for i in range(len(word)-1):
        for j in range(i+1,len(word)):
            swapped = swap(word,i,j)

            # if there is a match that is not the same word (e.g. misS vs miSs)
            if swapped in a_list and swapped != word:

                #store metathesis pair
                m_list.append((word,swapped))

                count+=1
                
                # Exit the function (and stop all of the loops) if max no. of pairs found
                if count == len(a_list)-1:
                    return 
                
def metathesis_list(anagram_list):
    ''' returns all meathesis pairs from a list of anagrams
    '''
    
    # list to store metathesis pairs
    m_list = []
    
    # create a copy of the anagram list that will get updated through the loop
    a_list = anagram_list[:]

    # check all combinations in the list
    # no need to go to last item in list because only 1 word in list after update
    while len(a_list) > 1:

        # store word to search and remove from list
        word = a_list[0]
        del a_list[0]
        metathesis_word(word, a_list, m_list)

    return m_list

def metathesis_all(filename):

    anagram_list = ana.make_anagram_list(filename)

    metathesis_pairs = []
    for set_anagrams in anagram_list:
        metathesis_pairs.append(metathesis_list(set_anagrams))

    return metathesis_pairs
        

t= metathesis_all('words.txt')

