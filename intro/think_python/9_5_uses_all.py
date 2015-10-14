def uses_all(word,letters):

    for letter in letters:
        if letter not in word:
            return False
    
    return True

if __name__ == '__main__':
    letters = 'aeiouy'

    fin = open('words.txt')

    count = 0
        
    for line in fin:
        word = line.strip()

        if uses_all(word,letters):
            print word
            count+=1      
        

    print count

    # 'aeiou' --> 598
    # 'aeiouy' --> 42
