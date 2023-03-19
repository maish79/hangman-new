"""
modules for hangman

"""


import random
import pyfiglet
import hangman_letters


def display_logo():
    """Displays the hangman logo"""
    logo = pyfiglet.figlet_format("welcome to\n Hangman",
                                  font="standard", justify="center")
    print(logo)


def get_player_name():
    """Prompts the player to enter their name and returns the name"""
    player_name = input("Please enter your name: ")
    return player_name


name = get_player_name()
print("Hello, " + name + "! Welcome to the game")


def get_guess(guessed_letters, all_letters):
    """
    Prompts the player to enter a letter and validates the input.
    Returns the guessed letter if it is a valid single
    letter not previously guessed.
    """
    while True:
        guess = input("Guess a letter:\n").lower()

        if len(guess) != 1:
            print("Please pick a single letter.")
        elif guess not in all_letters:
            print("Please make sure enter a letter.")
        elif guess in guessed_letters:
            print(f'You already guessed the letter {guess}, please try again.')
        else:
            return guess


def update_guessed(guess, guessed):
    """Updates the guessed letters with the newly guessed letter"""
    return guessed + guess


def update_blank(guess, word, blank):
    """
    Updates the blank spaces with the newly guessed
    letter if it is present in the word.
    Returns the updated blank spaces.
    """
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                blank[i] = guess
        print("Congrats you found a match")
    else:
        print(f"Sorry, {guess} is not in the word. Please, try again!")
    return blank


def update_lives(guess, word, lives):
    """
    Decreases the number of lives if the guessed
    letter is not present in the word.
    Returns the updated number of lives.
    """
    if guess not in word:
        lives -= 1
        print(f"You have {lives} lives left.")
    return lives


def play_hangman():
    """Plays a game of hangman"""
    hangman = ['''
 +---+
 |   |
 O   |
/|\\ |
/ \\ |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\\ |
  \\ |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\\ |
     |
     |
=======''', '''
+---+
 |   |
 O   |
/|   |
     |
     |
=======''', '''
+---+
 |   |
 O   |
 |   |
     |
     |
=======''', '''
+---+
 |   |
 O   |
     |
     |
     |
     |
=======''']

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lives = 6
    guessed = ""
    end_of_game = False
    word = random.choice(hangman_letters.word_list)

    display_logo()
    print("You have 6 attempts to guess the word!")

    blank = ["_"] * len(word)

    while not end_of_game:
        guess = get_guess(alphabet, guessed)
        guessed = update_guessed(guess, guessed)
        blank = update_blank(guess, word, blank)
        lives = update_lives(guess, word, lives)

        print(blank)
        print(hangman[lives])

        if "_" not in blank:
            print("Congratulations, you win!")
            end_of_game = True

        if lives == 0:
            print("You lose!")
            print("The word was " + word)
            end_of_game = True

    play_again_input = input("Do you want to play again? (y/n)").lower()
    if play_again_input == "y":
        play_hangman()


play_hangman()
