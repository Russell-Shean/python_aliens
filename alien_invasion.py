# alien_invasion.py

#import modules
import sys
import pygame

# Import the Settings class from the settings module
from settings import Settings
from ship import Ship

# Define an alien invasion class
class AlienInvasion:
	"""The is the overall class for the entire game"""


	def __init__(self):
		"""initialize the game and create some game resources"""

		# For this we use pygame's init() function
		pygame.init()


		# add an instance of the Settings() class to self
		self.settings = Settings()


		# This must set the screen size or something
		# Whytwo sets of parenthesis??
		#self.screen = pygame.display.set_mode((1920,1080))

		# New plan use settings to define screen size:
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_width))

		# This sets the title that shoows across the top of the window?
		pygame.display.set_caption("The Aliens are invading!       Can you help??")

		# set a new background color
		self.bg_color = (self.settings.bg_color)

		# Add the Ship class as an attribute to the game
		self.ship = Ship(self)


	def run_game(self):
		"""This method actually starts and runs the game inside the window"""

		while True:

			# creating a check events method
			self._check_events()
			# update events
			self._update_screen()
			# move the ship to the right
			self.ship.update_position()

	
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

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)



	def _check_keydown_events(self, event):
		"""respond to key presses"""


			

		# right key down
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True

		# left key down
		elif event.key == pygame.K_LEFT:
			# Move ship to left
			self.ship.moving_left = True


		# up key down
		elif event.key == pygame.K_UP:
			# Move the ship up
			self.ship.moving_up = True

		# down key down
		elif event.key == pygame.K_DOWN:
			# Move ship down
			self.ship.moving_down = True



	def _check_keyup_events(self, event):			

			
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False






	def _update_screen(self):
		"update images on screen and flip to next screen"

		# actually update the screen color
		self.screen.fill(self.bg_color)

		# draw the ship
		self.ship.blitme()

		# draw the most recent screen
		pygame.display.flip()



# Make the game an instance and run it


if __name__ == "__main__":

	ai = AlienInvasion()
	ai.run_game()







