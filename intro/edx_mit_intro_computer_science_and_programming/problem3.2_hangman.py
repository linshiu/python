# -*- coding: utf-8 -*-

"""
edX - MIT - Introduction to Computer Science and Programming
Problem Set 3 - Hangman
Python 2.7 - Adapted for python 3

"""

#%% Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os
WORDLIST_FILEPATH = "/Users/Steven/Documents/Professional/Data Science and Analytics/2_Courses/edX_Introduction_Computer_Science_and_Programming/problem_sets/ps03"
WORDLIST_FILENAME = "words.txt"

os.path.join(WORDLIST_FILEPATH, WORDLIST_FILENAME)

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    #inFile = open(os.path.join(WORDLIST_FILEPATH, WORDLIST_FILENAME), 'r', 0) # this is python 2
    inFile = open(os.path.join(WORDLIST_FILEPATH, WORDLIST_FILENAME), 'r') 
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    #wordlist = string.split(line) # this is for python 3
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

#%%
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            output += "_ "
        else:
            output += letter

    return output


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ''
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available += letter
            
    return available
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game, Hangman")
    print("I am thinking of a word that is {} letters long".format(len(secretWord)))
    
    # initialize variables
    lettersGuessed = [] #The letters that have been guessed so far.
    mistakesMade = 0 # The number of incorrect guesses made so far.
    availableLetters = string.ascii_lowercase #The letters that may still be guessed. 
    word_guessed = getGuessedWord(secretWord, lettersGuessed)
    correct_guess = False
    MAX_GUESSSES = 8
    
    # game stops when word guessed correctly or reach max number of guesses    
    while not correct_guess and mistakesMade < MAX_GUESSSES:  
        
        #use raw_input functoin for python 2.7
        letter_guess = input("-------------\n\n"
                             "You have {0} guesses left.\n"
                             "Available letters: {1}\n"
                             "Please guess a letter: ".format(MAX_GUESSSES - mistakesMade,
                                                              availableLetters)).lower()
        
        # duplicate guess
        if letter_guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: {}".format(word_guessed))
        
        # wrong guess: update guessed letter, available letters, mistakes
        elif letter_guess not in secretWord:
            lettersGuessed.append(letter_guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            mistakesMade += 1
            print ("Oops! That letter is not in my word: {}".format(word_guessed))
        
        # correct guess:  update guessed letter, available letters, word guessed
        # and if all letters guessed
        else:
            lettersGuessed.append(letter_guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            word_guessed = getGuessedWord(secretWord, lettersGuessed)
            correct_guess = isWordGuessed(secretWord, lettersGuessed)
            print ("Good guess: {}".format(word_guessed))
        
    
    print("\n-------------\n")
    
    if correct_guess:
        print ("Congratulations, you won!")
    else:
        print ("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


#%%

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
