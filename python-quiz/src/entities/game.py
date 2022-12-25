class Game:
    """ Game class consists of only a few attributes, which contains info
        about games status.
    """

    def __init__(self):
        """Constructor generates games starting values
        """
        self.player = ""
        self.rounds = 1
        self.score = 0
        self.running = False


    def increase_score(self):
        """Increases score with a solid increment of  value 1.
        """
        self.score += 1

    def set_player_name(self, name):
        """Sets player name

        Args:
            name (str): Player name
        """
        self.player = name
