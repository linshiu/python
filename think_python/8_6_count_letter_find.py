def find(word,letter,start):
    index = start
    while index < len(word):

        if word[index] == letter:
            return index
        
        index += 1
    return -1


def count_letter(word,letter):
    count = 0
    index = 0

    while True:
        index = find(word,letter,index)

        if index == -1:
            break

        index+=1
        count+=1

    print count


if __name__ == '__main__':
    count_letter('banana','b')
    
