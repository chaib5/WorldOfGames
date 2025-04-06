import random

difficulty = 0
secret_number = 0

def generate_number():
    global secret_number
    secret_num = random.randint(1,difficulty)
    secret_number = secret_num
    print(secret_number)


def get_guess_from_user():
    while True:
        try:
            num_user = int(input("Guess the number : "))
            print(num_user)
            return (num_user)
        except ValueError:
            print("Error value")

def compare_results(secret_number,user_number):
    if secret_number == user_number:
        return True
    else:
        return False

def play(level):
    global difficulty
    difficulty = level
    global secret_number
    generate_number()
    numUser = get_guess_from_user()
    if compare_results(secret_number, numUser) == True:
        print("Win")
        return True
    else:
        print('Loose')
        return False

# play()





