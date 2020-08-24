from classes.Sprite import Sprite
import pyxel

class Ball(Sprite):
	def __init__(self):
		super().__init__(
			x = pyxel.height / 2,
			y = pyxel.width / 2,
			u = 0,
			v = 8,
			w = 3,
			h = 3
		)
		self._speed_x = 0
		self._speed_y = 1.5

	def update(self):
		self._x = self.x + self._speed_x
		self._y = self.y + self._speed_y

		if (self.x <= 2 or self.x >= pyxel.width - 2):
			self._speed_x = self._speed_x * -1

		if (self.y <= 2 or self.y >= pyxel.height - 2):
			self._speed_y = self._speed_y * -1