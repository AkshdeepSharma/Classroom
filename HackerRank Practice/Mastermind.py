#!/usr/bin/env python3

import random as r

#Word Bank
WORD_BANK_VERY_EASY = ['DOZY', 'LAZY', 'FLUX', 'JEFE', 'WORD']
WORD_BANK_EASY = ['CRAZY', 'WORLD', 'HELLO', 'SCUZZ', 'JUJUS']
WORD_BANK_AVERAGE = ['LETTER', 'PUZZLE', 'YELLOW', 'FATHER', 'LENGTH']
WORD_BANK_HARD = ['QUIZZED', 'ZYGOTIC', 'ABANDON', 'MUMBLED', 'VIVIDLY']
WORD_BANK_VERY_HARD = ['ATHLETIC', 'CHEMICAL', 'RELATIVE', 'OPPONENT', 'WORKSHOP']

#Selects a random word from the word bank, given the difficulty.
def Selected_Word(difficulty):
    return {
        1: WORD_BANK_VERY_EASY[r.randrange(0, 4)],
        2: WORD_BANK_EASY[r.randrange(0, 4)],
        3: WORD_BANK_AVERAGE[r.randrange(0, 4)],
        4: WORD_BANK_HARD[r.randrange(0, 4)],
        5: WORD_BANK_VERY_HARD[r.randrange(0, 4)]
        }[difficulty]       

#Compares the guessed word to the 
def User_Guess(guessedWord, selectedWord):
    counter = 0
    for x, y in zip(guessedWord, selectedWord):
        if x == y:
            counter += 1
    print("Number of letters in the right position: " + str(counter) + "/" + str(len(selectedWord)))
    return counter

#main
if __name__ == "__main__":
    print("Welcome to mastermind. All guesses must be made in CAPS.")
    print('')
    
    selectedWord = Selected_Word(int(input("Enter a difficulty from 1-5: ")))
    
    print("A word has been selected. You have 5 guesses!")
    print('')
    
    numberOfGuesses = 0
    
    while True:
        guessedWord = input("Enter in a word: ")
        counter = User_Guess(guessedWord, selectedWord)
        print('')
        num = counter / len(selectedWord)
        numberOfGuesses += 1
        if num == 1:
            print("You got the word!")
            break
        elif numberOfGuesses == 5:
            print("You ran out of guesses. Better luck next time.")
            break