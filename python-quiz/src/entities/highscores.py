from services.highscore_services import save_to_file

class Highscores:
    """Class which resembles highscore

    Attributes:
        name = player name
        score = player score
        date = datetime today in str
    """
    def __init__(self, name, score, date):
        """Constructor to create highscore object.

        Args:
            name (str): _description_
            score (int): _description_
            date (str): _description_
        """
        self.name = name
        self.score = score
        self.date = date


    def save_score(self):
        """ Method which saves Highscore to a .csv file
        """
        save_to_file(self)
