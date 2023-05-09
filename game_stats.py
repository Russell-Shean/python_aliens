# game_stats.py

class GameStats:
	"""Track game statistics"""

	def __init__(self, ai_game):
		"""start a fresh instance of the game's statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""reset stats at the biggening of a new game"""
		self.ships_left = self.settings.ship_limit

	