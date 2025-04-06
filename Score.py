import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

#Functiom to add a score
def add_score(difficulty):
    points = (difficulty * 3) + 5

    try:
        # verify if the path exists and read the old score
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read())
        else:
            current_score = 0

        new_score = current_score + points
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

    except Exception as e:
        print(f"Error to add to the score: {e}")

    return BAD_RETURN_CODE