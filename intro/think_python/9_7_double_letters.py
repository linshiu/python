def index_double(word,start):
    '''returns the index of the second letter of a double.
       If no double found, -1 is return'''
    i = start

    while i < len(word)-1:
        if word[i+1] == word[i]:
            return i+1
        i+=1
    return -1

def count_double(word):
    '''returns the number of  doubles'''

    count = 0
    
    i_start = index_double(word,0)

    print i_start
    
    while i_start != -1:
        count += 1
        i_start = index_double(word,i_start+1)

        print i_start

    return count

def is_3consecutive_doubles(word):
    '''returns the number of  doubles'''

    #find the index of first double
    i = index_double(word,0)

    # if there is a double
    if i != -1:

        # if the next two letters are doubles
        if index_double(word[i+1:i+3],0) != -1:
            
            # if the next two letters are doubles
            if index_double(word[i+3:i+5],0) != -1:
                
                return True

    return False

if __name__ == '__main__':
    fin = open('words.txt')

    count = 0
        
    for line in fin:
        word = line.strip()

        if is_3consecutive_doubles(word):
            count+=1
            print word

    print count
    
        
    

    
