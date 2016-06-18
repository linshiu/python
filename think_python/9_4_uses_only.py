def uses_only(word,letters):

    for letter in word:
        if letter not in letters:
            return False
    
    return True

if __name__ == '__main__':
    letters = 'acefhlo'

    fin = open('words.txt')

    count = 0
        
    for line in fin:
        word = line.strip()

        if uses_only(word,letters):
            print word
            count+=1      
        

    print count
        
