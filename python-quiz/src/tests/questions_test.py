import unittest
from repositories.questions import Questions
from connection import get_db_connection


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.a = Questions(get_db_connection())
        self.questions = self.a.get_questions()

    # Test for correct answer in answers.

    def test_correct_in_answers(self):
        correct = self.questions[0]
        answers = self.questions[2]
        assert correct in answers

    # Test for returned amount of answers.

    def test_amount_answers(self):
        self.answers_amount = len(self.questions[2])
        self.assertEqual(self.answers_amount, 4)

    # Test in case no capital city exist

    def test_for_no_capital(self):
        while self.questions[0] != "No capital city":
            self.questions = self.a.get_questions()
        answers = self.questions[2]

        assert "No capital city" in answers
