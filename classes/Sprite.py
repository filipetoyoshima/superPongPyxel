from abc import ABC, abstractmethod
from classes.AssetImg import AssetImg
import pyxel

class Sprite(ABC):
	@abstractmethod
	def __init__(self, x, y, u, v, w, h, img=None):
		self._x = x
		self._y = y
		self._asset_img = AssetImg(
			u = u,
			v = v,
			img = img or 0,
			w = w,
			h = h
		)

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def height(self):
		return self._asset_img._h

	@property
	def width(self):
		return self._asset_img._w

	def update(self):
		pass

	def intersects(self, sprite):
		if (
			abs(self.x - sprite.x) < ((self.width + sprite.width) / 2)
			and abs(self.y - sprite.y) < ((self.height + sprite.height) / 2)
		):
			return True
		return False

	def draw(self):
		self._asset_img.draw(self._x, self._y)