import MemoryGame
import GuessGame
import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    print("Hello", name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def updatedMainGame(game,level):
    if game == 1:
        won = MemoryGame.play(level)
    if game == 2:
        won = GuessGame.play(level)
    if game == 3:
        won = CurrencyRouletteGame.play(level)

    else:
        load_game()

    if won:
        add_score(level)  # update score
        print("Your score is update.")


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    choose_game = 0
    choose_level = 0

    while True:
        choose_game = (input("Choose the number of the GAME that you want to play (1 to 3): "))
        if choose_game.isdigit() and 1<= int(choose_game) <= 3:
            choose_game=int(choose_game)
            break

        else:
                print("Invalid choice.")

    while True:
        choose_level = (input("Choose the number of the LEVEL that you want (1 to 5): "))
        if choose_level.isdigit() and 1 <= int(choose_level) <= 5:
            choose_level = int(choose_level)
            break

        else:
            print("Invalid choice.")

    updatedMainGame(choose_game,choose_level)

