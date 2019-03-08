# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

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
    # FILL IN YOUR CODE HERE...
    for letters in secretWord:
        if letters in lettersGuessed:
            continue
        else :
            return False
    return True
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    p = ''
    for letters in secretWord:
        if letters in lettersGuessed:
            p += letters
        else :
            p +='_ '
    return p


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    p =''
    for letters in string.ascii_lowercase:
        if letters in lettersGuessed:
            continue
        else:
            p += letters
    return p
    

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
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    GuessLeft = 8
    wordLen = len(secretWord)

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(wordLen)+' letters long.')
    print('-----------')
    print('You have 8 guesses left.')
    print('Available Letters: abcdefghijklmnopqrstuvwxyz')
    #print("Please guess a letter: ")
    a = input("Please guess a letter: ") 
    a = a.lower()

    while GuessLeft > 0:
        if a in lettersGuessed:
            print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            #print("Please guess a letter: ")
            a = input("Please guess a letter: ") 
            a = a.lower()
            continue
        else:
            lettersGuessed += a 
            if isWordGuessed(secretWord, lettersGuessed):
                print("Good guess: "+ str(secretWord))
                print("------------")
                print("Congratulations, you won!")
                break
            else:
                if a in secretWord:
                    print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
                    print("------------")
                    print("You have "+str(GuessLeft)+" guesses left.")
                    print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
                    #print("Please guess a letter: ")
                    a = input("Please guess a letter: ") 
                    a = a.lower() 
                else:
                    GuessLeft -= 1
                    if GuessLeft == 0:
                        print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
                        print("------------")
                        print("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")
                        break
                    print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
                    print("------------")
                    print("You have "+str(GuessLeft)+" guesses left.")
                    print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
                   # print("Please guess a letter: ")
                    a = input("Please guess a letter: ")    
                    a = a.lower()
                
           


'''    
    while a in lettersGuessed:
        print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed)))
        print("------------")
        print("You have "+str(GuessLeft)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        a = input("Please guess a letter: ")
        a = a.lower()
        continue
        
        lettersGuessed += a 
        GuessLeft -= 1
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: "+ str(secretWord))
            print("------------")
            print("Congratulations, you won!")
            
        else:
            if GuessLeft == 0:
                print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
                print("------------")
                print("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")
            else:
                if a in secretWord:
                    print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
                    print("------------")
                    print("You have "+str(GuessLeft)+" guesses left.")
                    print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
                    a = input("Please guess a letter: ") 
                    a = a.lower() 
                else:
                    print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
                    print("------------")
                    print("You have "+str(GuessLeft)+" guesses left.")
                    print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
                    a = input("Please guess a letter: ")   
                    a = a.lower()


###################################
        if a in secretWord:
            print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            a = input("Please guess a letter: ") 
            a = a.lower()
        else:
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            a = input("Please guess a letter: ")   
            a = a.lower()
        continue
        
     
        
    print('-----------')
    print('You have 8 guesses left.')
    print('Available Letters: abcdefghijklmnopqrstuvwxyz')
    a = input('Please guess a letter: ')
    a = a.lower()
    isGinLG(a, lettersGuessed, GuessLeft)



    
    while (not isWordGuessed(secretWord, lettersGuessed)) and (GuessLeft >0):
        if a in lettersGuessed :
            print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            a = input("Please guess a letter: ")
            a = a.lower()
            continue
        else:
            lettersGuessed += a 
            GuessLeft -= 1
        
        if a in secretWord:
            print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            a = input("Please guess a letter: ") 
            a = a.lower()
            continue
        else:
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("You have "+str(GuessLeft)+" guesses left.")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            a = input("Please guess a letter: ")   
            a = a.lower()
            continue
    
    if isWordGuessed(secretWord, lettersGuessed):
        print("Good guess: "+ str(secretWord))
        print("------------")
        print("Congratulations, you won!")
    
    if GuessLeft == 0 :
        print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
        print("------------")
        print("Sorry, you ran out of guesses. The word was "+str(secretWord)+".")
'''
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
