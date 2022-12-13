import unittest
import os
from services.highscore_services import file_check
from services.highscore_services import read_data
from services.highscore_services import get_scores
from services.highscore_services import check_scores

dir = os.path.dirname(__file__) 
path = os.path.join(dir, "..", "..", "data", "highscores.csv")


class TestHighscoreServices(unittest.TestCase):

    def test_file_check(self):
        os.remove(path)
        a = file_check()
        self.assertEqual(a, True)

    def test_read_data(self):
        data = read_data()
        self.assertEqual(len(data), 2)

    def test_read_data_type(self):
        data = read_data()
        self.assertIsInstance(data[0], int)

    def test_get_scores(self):
        scores = get_scores()
        self.assertIsInstance(scores, list)

    def test_check_scores(self):
        a = check_scores(12)
        self.assertEqual(a, True)
