class Player:

    def __init__(self):
        self.name = ""
        self.score = 0


    def set_player_name(self, name):
        self.name = name


    def increase_score(self):
        self.score += 1


    def set_score_to_zero(self):
        self.score = 0

    