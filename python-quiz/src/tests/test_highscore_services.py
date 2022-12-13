import unittest
import os
from services.highscore_services import file_check
from services.highscore_services import read_data
from services.highscore_services import get_scores
from services.highscore_services import check_scores

dir = os.path.dirname(__file__) 
path = os.path.join(dir, "..", "..", "data", "highscores.csv")


class TestHighscoreServices(unittest.TestCase):

    # Test for file checker, first removing the file.

    def test_file_check(self):
        os.remove(path)
        a = file_check()
        self.assertEqual(a, True)

    # Test for reading data. returns tuple len of 2.

    def test_read_data(self):
        data = read_data()
        self.assertEqual(len(data), 2)

    # test for the tuple containing int.

    def test_read_data_type(self):
        data = read_data()
        self.assertIsInstance(data[0], int)

    # test for get_scores delivering list

    def test_get_scores(self):
        scores = get_scores()
        self.assertIsInstance(scores, list)

    # Test for score checker return value.

    def test_check_scores(self):
        a = check_scores(12)
        self.assertEqual(a, True)
