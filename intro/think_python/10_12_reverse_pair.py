'''
Two words are a reverse pair if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.'''

def bisect(word_list,target):

    t = word_list[:]

    # it gets updated after each bisection
    index = 0

    # keep deleting corresponding slices of the list (bisecting)
    # until a match is found or the list is empty
    while len(t)>0:

        # if there is a match, return the updated index
        if target == t[len(t)/2]:

            return index+len(t)/2
        
        # delete second half of the bisected list (no index update needed
        # since there is not offset after deleting the second half)
        elif target < t[len(t)/2]:

            del t[len(t)/2:]

        # delete first half of the bisected list (index gets updated to
        # index corresponding to the offset from the start of the new
        # bisected list
        else:
     
            index = index + len(t)/2 + 1
            del t[:len(t)/2+1]

    return None

def create_list():
    fin = open("words.txt")

    new = []
    for line in fin:
        word = line.strip()
        new.append(word)
    return new

def find_reverse():
    word_list = create_list()

    count = 0

    for word in word_list:
        if bisect(word_list,word[::-1]) != None:
            count += 1
            print word,word[::-1]
    print count

find_reverse()


def find_reverse2():
    word_list = create_list()

    count = 0

    for i in range(len(word_list)):
        
        j = i + 1
        while j < len(word_list):
           
            if is_reverse(word_list[i],word_list[j]):
                count+=1
                print word_list[i],",",word_list[j]

            j += 1
     
    print count   
