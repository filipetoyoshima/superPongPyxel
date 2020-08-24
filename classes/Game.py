from classes.Racket import Racket
import pyxel

class Game(object):
	def __init__(self):
		pyxel.init(80, 120, caption="Super Pong")
		pyxel.load('./../assets/resorces.pyxres')
		self.racket = Racket(1)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.racket.update()

	def draw(self):
		pyxel.cls(0)
		self.racket.draw()