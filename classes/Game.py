from classes.Racket import Racket
from classes.Ball import Ball
import pyxel

class Game(object):
	def __init__(self):
		pyxel.init(80, 120, caption="Super Pong")
		pyxel.load('./../assets/resorces.pyxres')
		self.racket = Racket(1)
		self.ball = Ball()
		self.sprites = [self.racket, self.ball]
		pyxel.run(self.update, self.draw)

	def update(self):
		for sprite in self.sprites:
			sprite.update()

	def draw(self):
		pyxel.cls(0)
		for sprite in self.sprites:
			sprite.draw()
			