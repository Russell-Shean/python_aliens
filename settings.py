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
		