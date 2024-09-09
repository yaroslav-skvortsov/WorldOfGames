import random
import time
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score  # Import the add_score function from Score.py
from Utils import screen_cleaner  # Optional: Import screen cleaner if needed


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play (1-3): "))
            if game_choice not in [1, 2, 3]:
                print("Invalid choice. Please choose a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please choose a number between 1 and 5.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Depending on the user's choice, play the respective game
    if game_choice == 1:
        game = MemoryGame(difficulty)
        if game.play():
            print("Congratulations! You remembered the sequence correctly.")
            add_score(difficulty)  # Add score if the player wins
        else:
            print(f"Sorry, the correct sequence was {game.sequence}. Better luck next time!")
    elif game_choice == 2:
        game = GuessGame(difficulty)
        if game.play():
            print("Congratulations! You guessed the number correctly.")
            add_score(difficulty)  # Add score if the player wins
        else:
            print(f"Sorry, the correct number was {game.secret_number}. Better luck next time!")
    elif game_choice == 3:
        game = CurrencyRouletteGame(difficulty)
        if game.play():
            print("Congratulations! You guessed the currency value correctly.")
            add_score(difficulty)  # Add score if the player wins
        else:
            print(f"Sorry, the correct value was around {game.amount_ils:.2f} ILS. Better luck next time!")
    else:
        print("Game not implemented yet.")