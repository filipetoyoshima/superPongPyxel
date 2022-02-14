import pyxel
from classes.AssetImg import AssetImg

OPEN_BRACKET = AssetImg(u=16, v=0, img=0, w=2, h=5)
CLOSE_BRACKET = AssetImg(u=19, v=0, img=0, w=2, h=5)
PURPLE_MARKER = AssetImg(u=22, v=1, img=0, w=1, h=3)
PINK_MARKER = AssetImg(u=24, v=1, img=0, w=4, h=3)
BRACKET_DISTANCE = 16

class Power(object):
    def __init__(self, player):
        self._power = 0
        self._x = pyxel.width / 2
        if player == 0:
            self._y = pyxel.height - 4
        else:
            self._y = 5

    def add_power(self, power):
        if power < 12:
            self._power = self._power + power

    def use_power(self):
        if self._power >= 4:
            self._power = self._power - 4
            return True
        return False

    @property
    def can_use(self):
        return self._power >= 4

    def draw(self):
        OPEN_BRACKET.draw(self._x, self._y)
        CLOSE_BRACKET.draw(self._x + BRACKET_DISTANCE, self._y)
        available_power = self._power // 4
        for i in range(available_power):
            PINK_MARKER.draw(self._x + (i * 5), self._y)
        for i in range(self._power % 4):
            PURPLE_MARKER.draw(self._x + available_power * 5 + 1 + i, self._y)
