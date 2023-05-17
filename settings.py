# settings.py

class Settings:
	"""A class to store all settings for the alien invasion game"""

	def __init__(self):
		"""Initialize the game's static settings class"""

		self.screen_width = 800
		self.screen_height = 800
		self.bg_color = (175, 238, 238)


		# ship limit
		self.ship_limit = 3

		
		# Bullet settings
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (220, 129, 160)
		self.bullets_allowed = 3

		# oranges settings
		self.oranges_allowed = 3

		# poop settings
		self.poops_allowed = 3

		# bigfoot settings
		self.fleet_drop_speed = 10



		# how fast things speed up
		self.speedup_scale = 1.1


		self.create_dynamic_settings()





	def create_dynamic_settings(self):

		# fleet direction: 1 is right, -1 is left
		self.fleet_direction = 1

		# adjust speed
		self.ship_speed = 1.5
		
		self.bullet_speed = 1.0

		self.orange_speed = 1.0

		self.poop_speed = 1.0

		self.bigfoot_speed = 0.5


	def increase_speed(self):
		"""Increase speed settings."""

		self.ship_speed *=self.speedup_scale
		self.bullet_speed *=self.speedup_scale
		self.orange_speed *=self.speedup_scale
		self.poop_speed *=self.speedup_scale
		self.bigfoot_speed *=self.speedup_scale

