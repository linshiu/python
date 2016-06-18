from __future__ import division  # single slash (/) for true (non-truncating) division.
                                 # (The // operator is used for truncating division.)

def has_no_e(word):
    if 'e' in word:
        return False
    return True

if __name__ == '__main__':

    fin = open('words.txt')

    count = 0
    total = 0
        
    for line in fin:
        word = line.strip()

        if has_no_e(word):
            count+=1      
        total+=1

    print count/total    
        
