import pyxel

class AssetImg(object):
	def __init__(self, u, v, img, w, h, x=None, y=None):
		self._x = x
		self._y = y
		self._u = u
		self._v = v
		self._img = img
		self._w = w
		self._h = h

	def draw(self, x=None, y=None):
		if (x == None):
			x = self._x
		else:
			x = x - self._w / 2

		if (y == None):
			y = self._y
		else:
			y = y - self._h / 2

		pyxel.blt(
			x = x,
			y = y,
			img = self._img,
			u = self._u,
			v = self._v,
			w = self._w,
			h = self._h
		)

	def update(self):
		pass