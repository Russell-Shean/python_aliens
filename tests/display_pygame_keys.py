#display_pygame_keys

#import modules
import sys
import pygame

from settings import Settings


# Define an alien invasion class
class DisplayKeysGame:
	"""The is the overall class for the entire game"""


	def __init__(self):
		"""initialize the game and create some game resources"""

		# For this we use pygame's init() function
		pygame.init()


		self.settings = Settings()


		# This must set the screen size or something
		# Whytwo sets of parenthesis??
		#self.screen = pygame.display.set_mode((1920,1080))

		# full screen stupid and not qorking...

		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = (self.screen.get_rect().height - 2000)

		# New plan use settings to define screen size:
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_width))

		# This sets the title that shoows across the top of the window?
		pygame.display.set_caption("The Aliens are invading!       Can you help??")

		# set a new background color
		self.bg_color = (self.settings.bg_color)


	def run_game(self):
		"""This method actually starts and runs the game inside the window"""

		while True:

			# creating a check events method
			self._check_events()
			# update events
			self._update_screen()
			# move the ship to the right
			#self.ship.update_position()


	def _check_events(self):
		"""respond to key presses and mouse events"""

		# here we watch for events that occur durin the game and execute depending on what they are
		for event in pygame.event.get():

			# If the event is quit we quit the game
			if event.type == pygame.QUIT:

				# This must be a system command to exit the current process
				sys.exit()

			# watch for key presses
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)



	def _check_keydown_events(self, event):
		"""respond to key presses"""
		print(f"You just pressed { event.key }")
		print(f"x = {pygame.K_x}\nc = { pygame.K_c }")


	def _update_screen(self):
		"update images on screen and flip to next screen"

		# actually update the screen color
		self.screen.fill(self.bg_color)







	


DisplayKeysGame().run_game()





