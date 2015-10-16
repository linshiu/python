def avoids(word,forbidden):

    for letter in word:
        if letter in forbidden:
            return False
    
    return True

if __name__ == '__main__':
    forbidden = raw_input('Enter a string of forbidden letters: ')

    fin = open('words.txt')

    count = 0
        
    for line in fin:
        word = line.strip()

        if avoids(word,forbidden):
            count+=1      
        

    print count

    #'aeiou' --> 107
        
