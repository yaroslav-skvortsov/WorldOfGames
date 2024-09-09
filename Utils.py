import os

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Function to clear the screen
def screen_cleaner():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')