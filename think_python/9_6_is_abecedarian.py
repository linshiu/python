def is_abecedarian(word):
    
    for i in range(len(word)-1):
        if word[i] >  word[i+1]:
            return False
    return True
    

if __name__ == '__main__':

    fin = open('words.txt')

    count = 0
        
    for line in fin:
        word = line.strip()

        if is_abecedarian(word):
            count+=1      

    print count

    #596
        
