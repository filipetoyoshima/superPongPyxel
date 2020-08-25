import pyxel

P1_X_COORD = 2
P1_Y_COORD = 2
P2_X_COORD = 2
P2_Y_COORD = 2
SCORE_STRING = "Score: "
SCORE_COLOR = 4

class Score(object):
    def __init__(self):
        self._scores = [0, 0]
        global P1_Y_COORD
        P1_Y_COORD = pyxel.height - 7
    
    @property
    def get(self, player):
        """
        Return the score of the player
        """
        return self._scores[player]
    
    def add_score_to_player(self, player):
        """
        Add a score point to the player in argument (0 or 1)
        Return False if player is not valid
        """
        try:
            self._scores[player] = self._scores[player] + 1
            return True
        except IndexError:
            return False

    def draw(self):
        pyxel.text(
            x = P1_X_COORD,
            y = P1_Y_COORD,
            s = (SCORE_STRING + str(self._scores[0])),
            col = SCORE_COLOR
        )

        pyxel.text(
            x = P2_X_COORD,
            y = P2_Y_COORD,
            s = (SCORE_STRING + str(self._scores[1])),
            col = SCORE_COLOR
        )