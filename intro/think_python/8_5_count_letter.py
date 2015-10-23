def count_letter(word,letter):
    count = 0
    for i in word:
        if i == letter:
            count+=1

    print count

if __name__ == '__main__':
    count_letter('banana','n')
