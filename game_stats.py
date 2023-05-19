# game_stats.py

import pandas

# read in high score from file
high_score_data = pandas.read_csv("high_score.csv")

# find the row where the maximum score occurs
highest_score_index = high_score_data['score'].idxmax()



# print(f"the user with the highest score is {} who scored {}")

# print(high_score_data['score'].idxmax())


class GameStats:
	"""Track game statistics"""

	def __init__(self, ai_game):
		"""start a fresh instance of the game's statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# start the game in active mode
		self.game_active = False


		# High score (it should never be reset)
		# read it in from file (above)

		# define the high_score
		self.high_score = high_score_data['score'][highest_score_index]
		# define the highest scoring user
		self.high_score_date = high_score_data['date'][highest_score_index]

		# define the historical data as an imutable variable
		self.high_score_historical = high_score_data['score'][highest_score_index]

		# define the historical data as a dictionary
		self.high_score_data = high_score_data


	def reset_stats(self):
		"""reset stats at the biggening of a new game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
	