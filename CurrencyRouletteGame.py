import random
import requests

difficulty = 0
exchange_rate = 0


def get_money_interval():
    global exchange_rate
    try:
        # Get the current exchange rate from USD to ILS using the API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]
        # print("exc ", exchange_rate)
        # Generate a random number between 1 and 100 (USD amount)
        usd_amount = random.randint(1, 100)
        # conversion usd to ils and interval correct
        correct_value = usd_amount * exchange_rate
        interval_min = correct_value - (5 - difficulty)
        interval_max = correct_value + (5 - difficulty)

        return interval_min, interval_max, correct_value, usd_amount

    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None, None, None, None


def get_guess_from_user():
    try:
        user_guess = float(input("try and guess the value of a random amount of USD in ILS: "))
        return user_guess
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_guess_from_user()


def play(level):
    global difficulty
    difficulty = level
    # style of calling a function and assigning the return values to the respective variables
    interval_min, interval_max, correct_value, usd_amount = get_money_interval()

    if interval_min is None:  # Error with fetching exchange rate
        print("Unable to fetch exchange rate. Please try again later.")
        return False

    # Print the USD amount for the user to guess
    print(f"Random USD amount: {usd_amount} USD")

    # Prompt the user for their guess
    user_guess = get_guess_from_user()

    # Check if the user's guess is within the interval
    if interval_min <= user_guess <= interval_max:
        print(f"Correct! The correct value for {usd_amount} USD is {correct_value:.2f} ILS.")
        return True  # User wins
    else:
        print(f"Wrong! The correct value for {usd_amount} USD is {correct_value:.2f} ILS.")
        print(
            f"Your guess was {user_guess:.2f}, but it should have been between {interval_min:.2f} and {interval_max:.2f}.")
        return False  # User loses


# play()
