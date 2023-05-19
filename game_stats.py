# game_stats.py

class GameStats:
	"""Track game statistics"""

	def __init__(self, ai_game):
		"""start a fresh instance of the game's statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# start the game in active mode
		self.game_active = False

	def reset_stats(self):
		"""reset stats at the biggening of a new game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		

	