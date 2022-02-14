from classes.Racket import Racket
from classes.Ball import Ball
from classes.Score import Score
import pyxel

class Game(object):
	def __init__(self):
		pyxel.init(80, 120, caption="Super Pong")
		pyxel.load('./../assets/resorces.pyxres')
		
		self.score = Score()

		self.players = [Racket(0), Racket(1)]
		self.ball = Ball(self.score.add_score_to_player)
		self.sprites = [self.players[0], self.players[1], self.ball]
		
		pyxel.run(self.update, self.draw)

	def update(self):
		for sprite in self.sprites:
			sprite.update()
		
		for player in self.players:
			if (self.ball.intersects(player)):
				player.notify_hit()
				self.ball.hit(player.speed)

	def draw(self):
		pyxel.cls(0)
		for sprite in self.sprites:
			sprite.draw()
		
		self.score.draw()