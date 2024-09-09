import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        # Check if the score file exists
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read())
        else:
            current_score = 0

        # Add the points of winning to the current score
        new_score = current_score + points_of_winning

        # Write the new score back to the file
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

    except Exception as e:
        print(f"An error occurred: {e}")
        return BAD_RETURN_CODE