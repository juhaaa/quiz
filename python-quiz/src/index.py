from entities.game import Game
from entities.highscores import Highscores
from services.highscore_services import print_scores
import datetime

if __name__ == "__main__":
    date = str(datetime.date.today())
    game = Game()
    result = game.play()
    score = Highscores("juha", result, date)
    score.save_score()
    print_scores()