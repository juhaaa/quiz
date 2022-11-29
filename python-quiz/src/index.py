from repositories.questions import Questions
from connection import get_db_connection
from entities.game import Game
from entities.player import Player

a = Questions(get_db_connection())
print(a.get_questions())
player = Player()
game = Game(player, a)
game.play()
