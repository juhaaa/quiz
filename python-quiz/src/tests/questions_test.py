import unittest
from questions import Questions

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.a = Questions()
        self.questions = self.a.get_questions(2)

    #Test for set amount.

    def test_amount(self):
        self.assertEqual(self.a.amount, 2)

    #Test for returned amount.

    def test_amount_questions(self):
        self.lenght = len(self.questions)
        self.assertEqual(self.lenght, 2)

    
