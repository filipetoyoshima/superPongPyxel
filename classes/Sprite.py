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

	def update(self):
		pass

	def draw(self):
		self._asset_img.draw(self._x, self._y)