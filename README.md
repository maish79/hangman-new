This is a simple hangman game written in Python. The game randomly selects a word from a pre-defined list and the player has to guess the word one letter at a time. The player has six attempts to guess the word. If the player is unable to guess the word in six attempts, the game is over.

Prerequisites
This game requires Python 3 to be installed on your system.

Getting Started
To start playing, simply run the play_hangman() function in your Python environment.

How to Play
The game will display the hangman logo and prompt the player to enter their name.
The player will be given six attempts to guess the word by entering one letter at a time.
If the player enters an invalid input or a letter they have already guessed, the game will prompt them to try again.
If the player correctly guesses a letter in the word, the letter will be revealed in its correct position.
If the player incorrectly guesses a letter, they will lose a life. The game will display a part of the hangman for each lost life.
The game ends when the player correctly guesses the word or runs out of lives.
The player can choose to play again after the game is over.
Acknowledgements
The list of words used in the game is provided by the hangman_letters module.