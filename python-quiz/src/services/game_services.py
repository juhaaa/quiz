from repositories.questions import Questions
from services.connection_services import get_db_connection
from entities.highscores import Highscores
from entities.game import Game
from ui.game_ui import game_interface_main, ui_correct_answer, ui_wrong_answer
import datetime


#init questions

def init_questions():
    question_object = Questions(get_db_connection())
    return question_object

#Start game

def start_game(stdscr):
    date = str(datetime.date.today())
    game = Game()
    result = play_game(game, stdscr)
    score = Highscores("", result, date)
    score.save_score(stdscr)

# main game loop, returns score

def play_game(game, stdscr):
    question_object = init_questions()
    game.running = True

    while game.running:
        question = question_object.get_questions()
        correct, country, answers = question[0], question[1], question[2]
        
        user_input = game_interface_main(stdscr, country, answers, game.score)
        if user_input == 0:
            break
        if check_correct(stdscr, game, correct, answers[user_input - 1]):
            game.increase_score()
        game.rounds += 1
        if game.rounds == 11:
            game.running = False

    return game.score


# checks answers outcome
# updates game- object accordingly

def check_correct(stdscr, game, correct, answer):
    if correct == answer:
        correct_string = f"You are correct. {correct} is the right answer!"
        ui_correct_answer(stdscr, correct_string)
        return True
    else:
        wrong_string = "Wrong answer!"
        ui_wrong_answer(stdscr, wrong_string)
        return False
