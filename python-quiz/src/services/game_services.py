import datetime
from repositories.questions import Questions
from services.connection_services import get_db_connection
from services.highscore_services import check_scores, file_check
from entities.highscores import Highscores
from entities.game import Game
from ui.game_ui import game_interface_main, ui_answer
from ui.highscore_ui import user_input_ui



#init questions

def init_questions():
    """ Initializes Questions object

    Returns:
        _Question: Class Question object which handles trivia questions.
    """
    question_object = Questions(get_db_connection())
    return question_object

#Start game

def start_game(stdscr):
    """Start game handles events in case player starts game.
        it runs the game, and checks if the the score will be saved,
        and gathers user input if needed for the name.

    Args:
        stdscr (Window): Curses Window object for displaying game
    """
    date = str(datetime.date.today())
    game = Game()
    result = play_game(game, stdscr)
    file_check()
    if check_scores(result):
        player_name = user_input_ui(stdscr)
        score = Highscores(player_name, result, date)
        score.save_score()


def play_game(game, stdscr):
    """Main game loop. Runs while game rounds < 11.

    Args:
        game (Game): Game object for scorekeeping and round count.
        stdscr (Window): Curses Window object for displaying game

    Returns:
        int: score after the game is played
    """
    question_object = init_questions()
    game.running = True

    while game.running:
        question = question_object.get_questions()
        correct, country, answers = question[0], question[1], question[2]
        user_input = game_interface_main(stdscr, country, answers, game.score)

        if check_correct(correct, answers[user_input - 1]):
            game.increase_score()
            ui_answer(stdscr, f"You are correct. {correct} is the right answer!")
        else:
            ui_answer(stdscr, "Wrong answer!")
        game.rounds += 1
        if game.rounds == 11:
            game.running = False

    return game.score


def check_correct(correct, answer):
    """Checks answers outcome.
    Returns boolean to update game- object accordingly

    Args:
        correct (str): correct answer
        answer (str): players answer

    Returns:
        boolean: status of answer being correct or not
    """
    if correct == answer:
        return True
    return False
