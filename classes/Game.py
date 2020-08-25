from classes.Racket import Racket
from classes.Ball import Ball
import pyxel

class Game(object):
	def __init__(self):
		pyxel.init(80, 120, caption="Super Pong")
		pyxel.load('./../assets/resorces.pyxres')
		
		self.players = [Racket(0), Racket(1)]
		self.ball = Ball()
		self.sprites = [self.players[0], self.players[1], self.ball]
		
		pyxel.run(self.update, self.draw)

	def update(self):
		for sprite in self.sprites:
			sprite.update()
		
		for player in self.players:
			if (self.ball.intersects(player)):
				print(player._player, player.speed)
				self.ball.hit(player.speed)

	def draw(self):
		pyxel.cls(0)
		for sprite in self.sprites:
			sprite.draw()
			