import unittest
from entities.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_score_zero(self):
        self.assertEqual(self.player.score, 0)

    def test_score_addition(self):
        for i in range(100):
            self.player.increase_score()
        self.assertEqual(self.player.score, 100)

    def test_player_name(self):
        self.player.set_player_name("Matti")
        self.assertEqual(self.player.name, "Matti")

    def test_setting_score_to_zero(self):
        for i in range(100):
            self.player.increase_score()

        self.player.set_score_to_zero()

        self.assertEqual(self.player.score, 0)
