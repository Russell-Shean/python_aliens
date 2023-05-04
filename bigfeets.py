# bigfeets.py

import pygame
from pygame.sprite import Sprite

class Bigfoot(Sprite):
	"""A Myfical Mafical Woodland Creature Frolicking through the mossy forests of the PNW"""

	def __init__(self, ai_game):
		"""Initialize some Bigfeeeetssss!!"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings


		# Load the bigfoot's glossy 9 by 7
		self.image = pygame.image.load("images/bigfoot_7.png")
		self.rect = self.image.get_rect()


		# Start the bigfeets at the top left corner
		self.rect.x = self.rect.width / 2
		self.rect.y = self.rect.height  / 2


		# store horizontal position as a float
		self.x = float(self.rect.x)


	def update(self):
		"""Move the alient to the right."""
		self.x += self.settings.bigfoot_speed
		self.rect.x = self.x