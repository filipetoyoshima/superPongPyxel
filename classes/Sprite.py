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