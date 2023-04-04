# ship.py 

# import the pygame module
import pygame

class Ship:
	"""A class for the ships, only we're doing garden gnomes"""

	def __init__(self, ai_game):
		"""create the ship and define its start position"""

		# get the screen's rectangle
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# load the gnome and get its bounding rectangle
		self.image = pygame.image.load("images/fairy.png")
		self.rect = self.image.get_rect()


		# always start ships at the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom


		# add a flag to check for movement
		self.moving_right = False


	def update_position(self):
		"""update the ship's position if the moving flag is true"""
		if self.moving_right:
			self.rect.x += 1

	
	def blitme(self):
		"""draw the gnome at its starting location"""
		self.screen.blit(self.image, self.rect)