import unittest
import os
import csv
from services.highscore_services import file_check
from services.highscore_services import read_data
from services.highscore_services import get_scores
from services.highscore_services import check_scores
from services.highscore_services import save_to_file
from entities.highscores import Highscores
import datetime

dir = os.path.dirname(__file__) 
path = os.path.join(dir, "..", "..", "data", "highscores.csv")


class TestHighscoreServices(unittest.TestCase):

    # Test for file checker, first removing the file, but maintaining scores.

    def test_file_check(self):
        scores = []
        with open(path, "r", encoding='UTF8') as file:
            for row in file:
                scores.append(row.strip().split(","))
        scores = scores[:10]
        scores.sort(key= lambda x: int(x[1]), reverse= True)
        os.remove(path)
        a = file_check()

        with open(path, "w", encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for row in scores:
                writer.writerow(row)
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

    # Test saving highscore to file without corrupting data.

    def test_save_to_file(self):
        file_check()
        original_scores = []

        with open(path, "r", encoding='UTF8') as file:
            for row in file:
                original_scores.append(row.strip().split(","))
        original_scores = original_scores[:10]
        original_scores.sort(key= lambda x: int(x[1]), reverse= True)

        date = str(datetime.date.today())
        a = Highscores("Elite", 20, date )
        save_to_file(a)

        test_manipulated_score = []

        with open(path, "r", encoding='UTF8') as file:
            for row in file:
                test_manipulated_score.append(row.strip().split(","))
        test_manipulated_score = test_manipulated_score[:10]
        test_manipulated_score.sort(key= lambda x: int(x[1]), reverse= True)

        test_outcome = False

        for i in range(len(test_manipulated_score)):
            if test_manipulated_score[i][0] == "Elite" and test_manipulated_score[i][1] == "20":
                test_outcome = True
                print("jee")
                break

        with open(path, "w", encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for row in original_scores:
                writer.writerow(row)

        self.assertEqual(test_outcome, True)
