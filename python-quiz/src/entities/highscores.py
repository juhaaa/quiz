from services.highscore_services import save_to_file

class Highscores:

    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date


    def save_score(self):
        save_to_file(self)
