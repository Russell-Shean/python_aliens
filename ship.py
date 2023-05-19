# ship.py 

# import the pygame module
import pygame

class Ship:
	"""A class for the ships, only we're doing garden gnomes"""

	def __init__(self, ai_game):
		"""create the ship and define its start position"""

		# get the screen's rectangle
		self.screen = ai_game.screen
		self.settings = ai_game.settings


		self.screen_rect = ai_game.screen.get_rect()

		# load the gnome and get its bounding rectangle
		self.image = pygame.image.load("images/fairy.png")
		self.rect = self.image.get_rect()


		# always start ships at the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's horizontal position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


		# add a flag to check for movement
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	# Now we define an update method for general updatings


	def update_position(self):
		"""update the ship's position if the moving flag is true"""

		# update the ship's x value instead of rect
		# limit x movement to edge of screen
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		if self.moving_up:
			self.y -= self.settings.ship_speed

		if self.moving_down:
			self.y += self.settings.ship_speed

		# update rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	
	def blitme(self):
		"""draw the gnome at its starting location"""
		self.screen.blit(self.image, self.rect)


	def _center_ship(self):
		"""
		Center the ship on the screen
		At the bottom
		"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)