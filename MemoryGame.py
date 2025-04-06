import time
import random

difficulty = 0  # Set the difficulty (number of elements in the list)

def generate_sequence():
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    print("Sequence generated:", sequence)  # You can remove this print statement when testing
    return sequence

def get_list_from_user():
    while True:
        try:
            user_input = input(f"Enter the {difficulty} numbers you remember, separated by spaces: ")

            user_list = [int(x) for x in user_input.split()]
            return user_list

        except ValueError:
            print("Error value")


def is_list_equal(list1, list2):
    return list1 == list2

def play(level):
    global difficulty
    difficulty = level
    sequence = generate_sequence()
    time.sleep(0.7)  # Adjust as needed to simulate the time the user sees the sequence
    print("\n" * 100)  # Clear the screen (this is just for simulation)
    user_guess = get_list_from_user()
    if is_list_equal(sequence, user_guess):
        print("Congratulations! You remembered the sequence correctly!")
        return True  # User wins
    else:
        print("Sorry, you didn't remember the sequence correctly. You lose!")
        return False  # User loses



# play()