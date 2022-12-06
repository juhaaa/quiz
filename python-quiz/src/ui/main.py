from entities.game import Game
from entities.highscores import Highscores
from services.highscore_services import print_scores
import datetime



# Text main-menu 

def main():

    print("welcome to capital quiz!")

    while True:
        print("0: Quit")
        print("1: Play")
        print("2: Highscores\n")
        choice = get_input()
        if choice == 0:
            break
        elif choice == 1:
            start_game()
        elif choice == 2:
            highscores()
            

def start_game():
    date = str(datetime.date.today())
    game = Game()
    result = game.play()
    score = Highscores("juha", result, date)
    score.save_score()

def highscores():
    print_scores()


# get user input

def get_input():
    valid = [0, 1, 2]
    while True:
        user_input = input("Choose between 1-2, zero ends: \n")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Input not valid, try again")
            continue
        if user_input in valid:
            break
        print("Input not valid, try again!")
    return user_input
