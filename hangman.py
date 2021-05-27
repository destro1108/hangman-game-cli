import random
import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    for sw in secret_word:
        if sw not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''

    return "".join(x for x in string.ascii_lowercase if x not in letters_guessed)

def display_hangman_image(wrong_inputs):
    '''
    prints the hangman image
    wrong_input: number of wrong input
    '''

    print(IMAGES[wrong_inputs], end="\n\n")

def is_valid_input(input):
    '''
    input: input given by the user
    returns: 
      returns if the input is valid (type boolean)
    '''

    return True if len(input) == 1 and input.lower() in string.ascii_lowercase else False


def get_hint(secret_word, letter_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return a character that hasn't been guessed by the user
    '''

    return random.choice(list(set(list(secret_word)).difference(set(letter_guessed))))

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:
    * In the beginning of the game you will know about the total characters in the secret_word    
    * In each round you have to guess one character
    * Partial word guessed by the user will be displayed    
    '''
    
    print("Welcome to the game, Hangman!")
    remaining_lives, wrong_inputs = 8, 0
    letters_guessed = []
    is_hint_used = False
    while remaining_lives > 0:
        print("I am thinking of a word that is {} letters long.".format(
            str(len(secret_word))), end='\n\n')

        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        if guess.lower() == "hint":
            if not is_hint_used:
                is_hint_used = True
                print("\n\t\tYou're hint is : {}".format(get_hint(secret_word, letters_guessed)),end="\n\n")
            else:
                print("\n\t\tYou've already used your hint!!!",end="\n\n")
            continue
        if not is_valid_input(guess):
            print("Please give Valid Input. Input should be a single character between a-z",end="\n\n")
            continue
        letter = guess.lower()
        letters_guessed.append(letter)

        if letter in secret_word:
            #letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            wrong_inputs += 1
            remaining_lives -= 1
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            #letters_guessed.append(letter)
            print("\nLives Remaining : {}".format(remaining_lives))
            print("",end="\n")
            display_hangman_image(wrong_inputs)


# driver code
secret_word = choose_word()
#print(secret_word)
hangman(secret_word)

