from classes.Sprite import Sprite
import pyxel

class Ball(Sprite):
	def __init__(self, score_updater):
		super().__init__(
			x = pyxel.width / 2,
			y = pyxel.height / 2,
			u = 0,
			v = 8,
			w = 3,
			h = 3
		)
		self._speed_x = 0
		self._speed_y = 1.5
		self._score_updater = score_updater

	def update(self):
		self._x = self.x + self._speed_x
		self._y = self.y + self._speed_y

		if (self.x <= 2 or self.x >= pyxel.width - 2):
			self._speed_x = self._speed_x * -1

		if (self.y <= 2):
			self._score_updater(0)
			self.reset_ball(1)
		elif (self.y >= pyxel.height - 2):
			self._score_updater(1)
			self.reset_ball(0)

	def reset_ball(self, player):
		speed_y = 0
		
		if (player == 0):
			speed_y = 1.5
		elif (player == 1):
			speed_y = -1.5
		else:
			raise IndexError
		
		self._x = pyxel.width / 2
		self._y = pyxel.height / 2
		self._speed_x = 0
		self._speed_y = speed_y
		

	def hit(self, speed=0):
		self._speed_y = self._speed_y * -1
		self._speed_x = self._speed_x + speed
