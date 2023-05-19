# bigfeets.py

import pygame
from pygame.sprite import Sprite

class Bigfoot(Sprite):
	"""A magical Woodland Creature Frolicking through the mossy forests"""

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


	def check_edges(self):
		"""Return True if Alien is at edge of screen"""
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right + 500 or self.rect.left <= -500 :
			return True


	def update(self):
		"""Move the alient to the right or left"""
		self.x += (self.settings.bigfoot_speed * self.settings.fleet_direction ) 
		self.rect.x = self.x



