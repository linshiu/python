def display_backwards(s):
    index = 0
    while index < len(s):
        print s[-(index+1)]
        index+=1

def backward_with_lines(word):
    index = len(word)
    while index > 0:
        print word[index-1]
        index = index -1


if __name__ == '__main__':
    display_backwards('123')
    
