from abc import ABC, abstractmethod
from classes.AssetImg import AssetImg
import pyxel

class Sprite(ABC):
	_x = NotImplemented
	_y = NotImplemented
	_asset_img = AssetImg(0, 0, 0, 0, 0, 0, 0)

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