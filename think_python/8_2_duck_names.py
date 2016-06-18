def duck_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            letter = letter+'u'
        print letter+suffix

if __name__ == '__main__':
    duck_names()
