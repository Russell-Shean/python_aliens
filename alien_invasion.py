# alien_invasion.py

#import modules
import sys
from time import sleep


import pygame

# Import the Settings class from the settings module
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard

from ship import Ship
from bullet import Bullet
from oranges import Orange
from poops import Poop
from bigfeets import Bigfoot

from button import Button

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


		# Create an instance of the scoreboard and
		# create a game statistics instance to store game data
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		# set a new background color
		self.bg_color = (self.settings.bg_color)

		# Add the Ship class as an attribute to the game
		self.ship = Ship(self)

		# add bullets together as a group
		self.bullets = pygame.sprite.Group()

		# vestigal thing for oranges
		self.oranges = pygame.sprite.Group()

		self.poops = pygame.sprite.Group()

		self.bigfeets = pygame.sprite.Group()

		self._create_fleet()

		# add a play button
		self.play_button = Button(self, "Start Game")




	def run_game(self):
		"""This method actually starts and runs the game inside the window"""

		while True:

			# creating a check events method
			self._check_events()


			if self.stats.game_active:
				# update events
				

				# move the ship to the right
				self.ship.update_position()

				# update projectiles
				self._update_projectiles()

				self._update_bigfeets()


			self._update_screen()

			

	
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


			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)



	def _check_play_button(self, mouse_pos):
		"""Start the game if the play clicks the play button"""

		button_clicked = self.play_button.rect.collidepoint(mouse_pos)

		if button_clicked and not self.stats.game_active:

		# if the mouse click's position overlaps the play button's position  and the game isn't already active reset the game and change the game status to active:

			# Reset game statistics settings whatever (variable settings?)
			# self.stats.reset_stats()
			self.settings.create_dynamic_settings()


			self.stats.game_active = True

			# remove extra aliens and projectiles
			self.bigfeets.empty()

			self.bullets.empty()
			self.oranges.empty()
			self.poops.empty()

			#create aliens and center ship
			self._create_fleet()
			self.ship._center_ship()

			# hide the mouse when the game is active
			pygame.mouse.set_visible(False)








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

		elif event.key == pygame.K_d:
			self._drop_poop()



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


	def _drop_poop(self):
		"""drop and new poop and add it to the pile"""

		if len(self.poops) < self.settings.poops_allowed:
			new_poop = Poop(self)
			self.poops.add(new_poop)



	def _update_projectiles(self):
		"""update position of bullets and delete old ones"""

		# check bullets and oranges
		self.bullets.update()
		self.oranges.update()
		self.poops.update()
		

		# get rid of old bullets and oranges
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


		for orange in self.oranges.copy():
			if orange.rect.bottom <= 0:
				self.oranges.remove(orange)


		for poop in self.poops.copy():
			if poop.rect.bottom >= self.settings.screen_height + 100:
				self.poops.remove(poop)

		self._detect_bigfoot_projectile_collisions()



	def _detect_bigfoot_projectile_collisions(self):


		# check to see if any projectiles have hit aliens and if so remove the aliens
		collisions_bullets = pygame.sprite.groupcollide(
			self.bullets, self.bigfeets, True, True)

		collisions_oranges = pygame.sprite.groupcollide(
			self.oranges, self.bigfeets, False, True)


		collisions_poops = pygame.sprite.groupcollide(
			self.poops, self.bigfeets, False, True)


		# remove bullets and recreate fleet after fleet destruction
		if not self.bigfeets:
			# Destroy existing projectiles and create new fleet.
			self.bullets.empty()
			self.oranges.empty()
			self.poops.empty()

			self._create_fleet()

			# up the speed each time a new fleet is regenerated
			self.settings.increase_speed()


	def _update_bigfeets(self):
		
		"""
		Check if a the fleet is at a horizontal edge, 
		then
		update the position of all the bigfoots in the troupe
		"""
		self._check_fleet_edges()
		self.bigfeets.update()


		# check for bigfoot gnome collisions
		if pygame.sprite.spritecollideany(self.ship, self.bigfeets):
			# print("Abandon ship!! We've been hit!!")
			self._ship_hit()


		self._check_bigfoot_bottom()

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien"""

		if self.stats.ships_left > 0:
			# reduce the number of ships left
			self.stats.ships_left -= 1

			# Get rid of any remaiing aliens and bullets.
			self.bigfeets.empty()
			self.bullets.empty()
			self.oranges.empty()
			self.poops.empty()

			# Create a new fleet and center the ship
			self._create_fleet()
			self.ship._center_ship()

			# Pause
			sleep(0.5)


		else: 
			self.stats.game_active = False
			pygame.mouse.set_visible(True)








	def _create_fleet(self):
		"""create a troupe of bigfeets"""
		# make a bigfoot
		bigfoot = Bigfoot(self)
		bigfoot_width, bigfoot_height = bigfoot.rect.size

		# define bigfoot width
		bigfoot_width = bigfoot.rect.width

		# define available space
		available_space_x = self.settings.screen_width - bigfoot_width
		number_bigfoot_x = available_space_x // bigfoot_width


		# determine how many rows will fit on screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
			                      (3 * bigfoot_height) - ship_height )

		number_rows = available_space_y // (2* bigfoot_height)



		# Create a full fleet of aliens
		for row_number in range(number_rows):
			# Create the first row of aliens
			for bigfoot_number in range(number_bigfoot_x):
				self._create_bigfoot(bigfoot_number, row_number)



	def _create_bigfoot(self, bigfoot_number, row_number):
		"""Create a bigfoot and put in a row"""
		bigfoot = Bigfoot(self)
		# define bigfoot width
		bigfoot_width, bigfoot_height = bigfoot.rect.size

		bigfoot.x = bigfoot_width + 2 * bigfoot_width * bigfoot_number
		bigfoot.rect.x = bigfoot.x
		bigfoot.rect.y = bigfoot_height + 2 * bigfoot.rect.height * row_number
		self.bigfeets.add(bigfoot)

		
	def _check_fleet_edges(self):
		"""change the fleet direction flag if the aliens have reached an edge"""
		for bigfoot in self.bigfeets.sprites():
			if bigfoot.check_edges():
				self._change_fleet_direction()
				break


	def _change_fleet_direction(self):
		"""drop the entire fleet vertically and change the horizontal direction"""
		for bigfoot in self.bigfeets.sprites():
			bigfoot.rect.y += self.settings.fleet_drop_speed 

		self.settings.fleet_direction *= -1



	def _check_bigfoot_bottom(self):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for bigfoot in self.bigfeets.sprites():
			if bigfoot.rect.bottom >= screen_rect.bottom:
				# Treat this the same as if the ship got hit. 
				self._ship_hit()
				break



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

		# draw poops
		for poop in self.poops.sprites():
			poop.draw_poop()

		# draw them bigfeets
		self.bigfeets.draw(self.screen)

		# draw the scoreboard on the screen
		self.sb.show_score()


		# draw a play button if the game is inactive
		if not self.stats.game_active:
			self.play_button.draw_button()






		# draw the most recent screen
		pygame.display.flip()










# Make the game an instance and run it


if __name__ == "__main__":

	ai = AlienInvasion()
	ai.run_game()







