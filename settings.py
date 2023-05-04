# settings.py

class Settings:
	"""A class to store all settings for the alien invasion game"""

	def __init__(self):
		"""Initialize the game settings class"""

		self.screen_width = 800
		self.screen_height = 800
		self.bg_color = (175, 238, 238)

		# adjust speed
		self.ship_speed = 1.5
		
		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (220, 129, 160)
		self.bullets_allowed = 3

		# oranges settings
		self.orange_speed = 1.0
		self.oranges_allowed = 3

		# poop settings
		self.poop_speed = 1.0
		self.poops_allowed = 3

		# bigfoot settings
		self.bigfoot_speed = 1.0

