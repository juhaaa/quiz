class Game:

    def __init__(self):
        self.player = ""
        self.rounds = 1
        self.score = 0
        self.running = False


    def set_player_name(self, name):
        self.player = name

    def increase_score(self):
        self.score += 1
