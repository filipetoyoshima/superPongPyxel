from abc import ABC, abstractmethod
import pyxel

class Sprite(ABC):
	_x = NotImplemented
	_y = NotImplemented
	_img = NotImplemented
	_u = NotImplemented
	_v = NotImplemented
	_w = NotImplemented
	_h = NotImplemented

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	def update(self):
		pass

	def draw(self):
		pyxel.blt(
			x = self.x,
			y = self.y,
			img = self._img,
			u = self._u,
			v = self._v,
			w = self._w,
			h = self._h
		)


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


class Game(object):
	def __init__(self):
		pyxel.init(80, 120, caption="Super Pong")
		pyxel.load('./resorces.pyxres')
		self.racket = Racket(1)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.racket.update()

	def draw(self):
		pyxel.cls(0)
		self.racket.draw()

Game()