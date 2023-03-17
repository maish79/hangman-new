import random
import hangman_letters

def display_logo():
    logo = '''
                      _                                             
                     | |                                            
                     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                     | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                     | | | | (_| | | | | (_| | | | | | | (_| | | | |
                     |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                         __/ |                      
                                        |___/    '''
    print(logo)

def get_player_name():
    name = input("\t\t\t\t\tEnter your name:")
    print("Welcome", name, "!")
    return name

def get_guess(a, guessed):
    while True:
        guess = input("Guess a letter:\n").lower()

        if len(guess) != 1:
            print("Please pick a single letter.")
        elif guess not in a:
            print("Please make sure enter a letter.")
        elif guess in guessed:
            print(f'You already guessed the letter {guess}, please try again.')
        else:
            return guess

def update_guessed(guess, guessed):
    return guessed + guess

def update_blank(guess, word, blank):
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                blank[i] = guess
        print("Congrats you found a match")
    else:
        print(f"Sorry, {guess} is not in the word. Please, try again!")
    return blank

def update_lives(guess, word, lives):
    if guess not in word:
        lives -= 1
        print(f"You have {lives} lives left.")
    return lives

def play_hangman():
    hangman = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\  |
  \  |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\  |
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

    a = set("abcdefghijklmnopqrstuvwxyz")
    lives = 6
    guessed = ""
    end_of_game = False
    word = random.choice(hangman_letters.word_list)

    display_logo()
    name = get_player_name()
    print("You have 6 attempts to guess the word!")

    blank = ["_"] * len(word)

    while not end_of_game:
        guess = get_guess(a, guessed)
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
