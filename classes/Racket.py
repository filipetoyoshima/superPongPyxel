from classes.Sprite import Sprite
from classes.Power import Power
import pyxel

class Racket(Sprite):
	def __init__(self, player):
		
		self._speed = 0
		self._power = Power(player)
		initial_position = 0

		if (player == 0):
			initial_position = pyxel.height - 10
			self._player = 1
			self._left_key = pyxel.KEY_A
			self._right_key = pyxel.KEY_D

		elif (player == 1):
			initial_position = 10
			self._player = 2
			self._left_key = pyxel.KEY_LEFT
			self._right_key = pyxel.KEY_RIGHT
		
		super().__init__(
			y = initial_position,
			x = pyxel.width / 2,
			u = 0,
			v = 0,
			img = 0,
			w = 16,
			h = 2
		)

	@property
	def speed(self):
		return self._speed

	def notify_hit(self):
		"""
		Notifies the Racket of a hit
		"""
		self._power.add_power(1)

	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		speed = 0
		if (pyxel.btn(self._left_key) and self.x > 8):
			speed -= 1
		if (pyxel.btn(self._right_key) and self.x < pyxel.width - 8):
			speed += 1

		self._speed = speed
		self._x = self.x + speed

	def draw(self):
		"""
		Draws the Racket
		"""
		self._power.draw()
		super().draw()