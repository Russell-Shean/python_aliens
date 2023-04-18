# alien_invasion.py

#import modules
import sys
import pygame

# Import the Settings class from the settings module
from settings import Settings
from ship import Ship
from bullet import Bullet
from oranges import Orange
from bigfeets import Bigfoot

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

		# Add the Ship class as an attribute to the game
		self.ship = Ship(self)

		# add bullets together as a group
		self.bullets = pygame.sprite.Group()

		# vestigal thing for oranges
		self.oranges = pygame.sprite.Group()

		self.bigfeets = pygame.sprite.Group()

		self._create_fleet()


	def run_game(self):
		"""This method actually starts and runs the game inside the window"""

		while True:

			# creating a check events method
			self._check_events()
			# update events
			self._update_screen()
			# move the ship to the right
			self.ship.update_position()

			# update projectiles
			self._update_projectiles()

			

	
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

		elif event.key ==pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

		elif event.key == pygame.K_f:
			self._fire_orange()



	def _check_keyup_events(self, event):			

			
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False




	# This method fires bullets

	def _fire_bullet(self):
		"""create a new bullet and add it to the bullet group"""

		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _fire_orange(self):
		"""add a new orange and add it to the orange group"""

		if len(self.oranges) < self.settings.oranges_allowed:
			new_orange = Orange(self)
			self.oranges.add(new_orange)



	def _update_projectiles(self):
		"""update position of bullets and delete old ones"""

		# check bullets and oranges
		self.bullets.update()
		self.oranges.update()
		

			# get rid of old bullets and oranges
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


		for orange in self.oranges.copy():
			if orange.rect.bottom <= 0:
				self.oranges.remove(orange)




	def _create_fleet(self):
		"""create a troup of bigfeets"""
		# make a bigfoot

		bigfoot = Bigfoot(self)
		self.bigfeets.add(bigfoot)

		



	def _update_screen(self):
		"update images on screen and flip to next screen"

		# actually update the screen color
		self.screen.fill(self.bg_color)

		# draw the ship
		self.ship.blitme()

		# draw bullets
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# draw oranges
		for orange in self.oranges.sprites():
			orange.draw_orange()

		# draw them bigfeets
		self.bigfeets.draw(self.screen)

		# draw the most recent screen
		pygame.display.flip()



# Make the game an instance and run it


if __name__ == "__main__":

	ai = AlienInvasion()
	ai.run_game()







