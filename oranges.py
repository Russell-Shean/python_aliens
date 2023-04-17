# oranges.py

# recreate the bullet class using a picture of an orange


import pygame
from pygame.sprite import Sprite

class Orange(Sprite):
	"""A class to manage all the bullets together as one group"""


	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""

		# This causes properties to be inherited from sprite
		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		#self.color = self.settings.bullet_color

		# create an orange rectangle at (0, 0) and then set its position
		self.image = pygame.image.load("images/small_orange.png")
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.ship.rect.midtop


		# store the bullet's position as a decimal value
		self.y = float(self.rect.y)




	def update(self):
		"""move the bullet across the screen"""

		# update the decimal position
		self.y -= self.settings.bullet_speed

		#update the position
		self.rect.y = self.y 
		

	
	
	def draw_orange(self):
		"""Draw the flying object onto the screen"""

		self.screen.blit(self.image, self.rect)