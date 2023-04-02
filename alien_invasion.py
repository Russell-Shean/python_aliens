# alien_invasion.py

#import modules
import sys
import pygame

# Define an alien invasion class
class AlienInvasion:
	"""The is the overall class for the entire game"""


	def __init__(self):
		"""initialize the game and create some game resources"""

		# For this we use pygame's init() function
		pygame.init()


		# This must set the screen size or something
		# Whytwo sets of parenthesis??

		self.screen = pygame.display.set_mode((1920,1080))

		# This sets the title that shoows across the top of the window?
		pygame.display.set_caption("The Aliens are invading!       Can you help??")

		# set a new background color
		self.bg_color = (175, 238, 238)


	def run_game(self):
		"""This method actually starts and runs the game inside the window"""

		while True:

			# here we watch for events that occur durin the game and execute depending on what they are
			for event in pygame.event.get():

				# If the event is quit we quit the game
				if event.type == pygame.QUIT:

					# This must be a system command to exit the current process
					sys.exit()


			# actually update the screen color
			self.screen.fill(self.bg_color)


			# draw the most recent screen
			pygame.display.flip()



# Make the game an instance and run it


if __name__ == "__main__":

	ai = AlienInvasion()
	ai.run_game()







