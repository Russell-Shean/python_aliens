# button.py

import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Define starting attributes for the button"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# set the button's dimmensions and colors
		self.width, self.height = 200, 5
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# build the button and center it
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center


		# Prepare the button's message (only needs to be done once)
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		"""Print a message onto a button"""

		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

		self.msg_image_rect = self.msg_image.get_rect()

		# center the message inside the button
		self.msg_image_rect.center = self.rect.center



	def draw_button(self):
		"""Draw the blank button plus message onto the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)