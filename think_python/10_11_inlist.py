
'''
To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.'''

'''
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary.'''

'''
You start in the middle and check to see whether the word you are looking for comes before the word
in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you
search the second half'''

''''Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it s not there.'''

'''Write a function called bisect that takes a sorted list and a target value and returns the index of
the value in the list, if it s there, or None if it s not.'''

'''
Or you could read the documentation of the bisect module and use that!'''


# note: function assumes python 2.7 where division is floor division
def bisect(word_list,target):

    t = word_list[:]

    # it gets updated after each bisection
    index = 0

    # keep deleting corresponding slices of the list (bisecting)
    # until a match is found or the list is empty
    while len(t)>0:

        # if there is a match, return the updated index
        if target == t[len(t)/2]:
            print 'check1 = '+str(index)
            return index+len(t)/2
        
        # delete second half of the bisected list (no index update needed
        # since there is not offset after deleting the second half)
        elif target < t[len(t)/2]:
            print 'check2 = '+str(index)
            del t[len(t)/2:]

        # delete first half of the bisected list (index gets updated to
        # index corresponding to the offset from the start of the new
        # bisected list
        else:
            print 'check3 = '+str(index)
            index = index + len(t)/2 + 1
            del t[:len(t)/2+1]

    return None
    
test = [0,1,2,3,4,5,6,7,8,9]

for i in test:
    x = bisect(test,i)
    print x


def create_list():

    fin = open('words.txt')
    new = []
    
    for line in fin:
        word = line.strip()
        new.append(word)    
    return new
            

def bisect2(word_list,target):

    t = word_list[:]

    index = 0
    i = 0

    while len(t)>0:
        
        i+=1

        if target == t[len(t)/2]:
            print 'check1 = '+str(index)
            print i
            return index+len(t)/2
        
        elif target < t[len(t)/2]:
            print 'check2 = '+str(index)
            del t[len(t)/2:]
        
        else:
            print 'check3 = '+str(index)
            index = index + len(t)/2 + 1
            del t[:len(t)/2+1]

    print i
    return None

words = create_list()
x = bisect2(words,'hello')
print x
print words[x]
