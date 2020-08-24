from classes.Sprite import Sprite
import pyxel

class Racket(Sprite):
	def __init__(self, player):
		if (player == 1):
			self._y = pyxel.height - 10
			self._x = pyxel.width / 2
			self._player = 1
			self._u = 0
			self._v = 0
			self._img = 0
			self._w = 16
			self._h = 2

	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)):
			self._x = self.x - 1
		elif (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)):
			self._x = self.x + 1