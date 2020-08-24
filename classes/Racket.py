from classes.Sprite import Sprite
from classes.AssetImg import AssetImg
import pyxel

class Racket(Sprite):
	def __init__(self, player):
		if (player == 1):
			self._y = pyxel.height - 10
			self._x = pyxel.width / 2
			self._player = 1
			self._asset_img = AssetImg(
				u = 0,
				v = 0,
				img = 0,
				w = 16,
				h = 2
			)

	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)):
			self._x = self.x - 1
		elif (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)):
			self._x = self.x + 1