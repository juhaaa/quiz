from services.game_services import play_game
class Game:

    def __init__(self):
        self.player = ""
        self.rounds = 0
        self.score = 0
        self.running = False
    
    def play(self):
        return play_game(self)
    
    def set_player_name(self, name):
        self.player = name

    def increase_score(self):
        self.score += 1

    def set_score_to_zero(self):
        self.score = 0