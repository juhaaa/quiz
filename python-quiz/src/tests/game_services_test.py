import unittest
from services.game_services import init_questions
from services.game_services import check_correct
from repositories.questions import Questions

class TestGameServices(unittest.TestCase):

    # Test for initializing questions object

    def test_init_questions(self):
        a = init_questions()
        self.assertIsInstance(a, Questions)

    # Test for correct answer check

    def test_check_correct(self):
        answer = check_correct("Helsinki", "Helsinki")
        self.assertEqual(answer, True )

    # Test for wrong answer check

    def test_check_wrong(self):
        answer = check_correct("Helsinki", "Stockholm")
        self.assertEqual(answer, False)