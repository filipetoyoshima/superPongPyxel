from abc import ABC, abstractmethod
import pyxel

class Sprite(ABC):
	_x = NotImplemented
	_y = NotImplemented

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	def update(self):
		pass

	def draw(self):
		pass


class Racket(Sprite):
	def __init__(self, player):
		if (player == 1):
			self._y = pyxel.height - 10
			self._x = pyxel.width / 2
			self._player = 1

	def update(self):
		"""
		Updates the Racket attributes depending on user input
		"""
		if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)):
			self._x = self.x - 1
		elif (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)):
			self._x = self.x + 1

	def draw(self):
		pyxel.pset(self.x, self.y, 11)
			


class Game(object):
	def __init__(self):
		pyxel.init (80, 120, caption="Super Pong")
		self.racket = Racket(1)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.racket.update()

	def draw(self):
		pyxel.cls(0)
		self.racket.draw()

Game()