# scoreboard.py

import pygame.font

class Scoreboard:
	"""A class to print the score out to the screen"""

	def __init__(self, ai_game):
		"""Define the startup state of an instance of Scoreboard"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font settings for the score info
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score image
		self.prep_score()


	def prep_score(self):
		"""Display the score as a rendered image"""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, 
			self.text_color, self.settings.bg_color)

		# display the score in the top right corner
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -20
		self.score_rect.top = 20 


	def show_score(self):
		"""Draw score on the screen"""
		self.screen.blit(self.score_image, self.score_rect)
