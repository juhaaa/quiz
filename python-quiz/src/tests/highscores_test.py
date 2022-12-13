import unittest
from entities.highscores import Highscores
import datetime



class TestHighscores(unittest.TestCase):
    
    def setUp(self):
        self.today = str(datetime.date.today())
        self.a = Highscores("Juha", 10, self.today)


    # Test for highscore.name

    def test_name(self):
        name = self.a.name
        self.assertEqual(name, "Juha")

    # Test for highscore.score

    def test_score(self):
        score = self.a.score
        self.assertEqual(score, 10)

    # Test for highscore.date

    def test_date(self):
        date = self.a.date
        self.assertEqual(date, str(datetime.date.today()))
