from classes.Sprite import Sprite
import pyxel

class Racket(Sprite):
	def __init__(self, player):
		if (player == 1):
			super().__init__(
				y = pyxel.height - 10,
				x = pyxel.width / 2,
				u = 0,
				v = 0,
				img = 0,
				w = 16,
				h = 2
			)
			self._player = 1


	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		if ((pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)) and self.x > 8):
			self._x = self.x - 1
		elif ((pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)) and self.x < pyxel.width - 8):
			self._x = self.x + 1