import unittest
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.a = Game()

    # Test for correct starting values

    def test_start_rounds(self):
        rounds = self.a.rounds
        self.assertEqual(rounds, 1)

    def test_start_running(self):
        running = self.a.running
        self.assertEqual(running, False)

    def test_start_score(self):
        score = self.a.score
        self.assertEqual(score, 0)

    # Test for setting player name

    def test_player_name(self):
        self.a.set_player_name("Matti")
        name = self.a.player
        self.assertEqual(name, "Matti")

    # Test increasing score

    def test_score_increase(self):
        self.a.increase_score()
        score = self.a.score
        self.assertEqual(score, 1)