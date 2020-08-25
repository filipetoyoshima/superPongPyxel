from classes.Sprite import Sprite
import pyxel

class Racket(Sprite):
	def __init__(self, player):
		if (player == 0):
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
			self._left_key = pyxel.KEY_A
			self._right_key = pyxel.KEY_D

		elif (player == 1):
			super().__init__(
				y = 10,
				x = pyxel.width / 2,
				u = 0,
				v = 0,
				img = 0,
				w = 16,
				h = 2
			)
			self._player = 2
			self._left_key = pyxel.KEY_LEFT
			self._right_key = pyxel.KEY_RIGHT


	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		if (pyxel.btn(self._left_key) and self.x > 8):
			self._x = self.x - 1
		elif (pyxel.btn(self._right_key) and self.x < pyxel.width - 8):
			self._x = self.x + 1