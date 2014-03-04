import pygame, sys, os
from pygame.locals import *

class Scroller(pygame.sprite.Sprite):
	''' A simple sprite that scrolls down the screen '''
	def __init__(self, screen, scroll_speed):

		''' Remember to pass the surface to the sprite for updating and drawing! '''
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		self.screen = screen
		self.scrolling = True
		
		# Load the image
		try:
			self.image = pygame.image.load('assets/ram_aras.png').convert_alpha()
			self.rect = self.image.get_rect()

			# Get the image's width and height
			self.image_w, self.image_h = self.image.get_size()

			# Get the screen's width and height
			self.screen_w = self.screen.get_size()[0]
			self.screen_h = self.screen.get_size()[1]
				
			# Set the (x, y)
			self.x = 0
			self.y = -1*(self.image_h - self.screen_h)
			
			# Set the scroll speed
			self.dy = 1
			
		except pygame.error, message:
			print "Cannot load background image!"
			raise SystemExit, message
				
	def update(self):
		''' Move the sprite if it still has room '''
		if ((self.y >= 0) and self.scrolling == True):
			return False
		else:
			self.y += self.dy
			return True

	def draw(self):
		''' Draw the sprite on the screen '''
		if self.scrolling == True:
			draw_pos = self.image.get_rect().move(self.x, self.y)
			self.screen.blit(self.image, draw_pos)
		else:
			draw_pos = self.image.get_rect().move(self.x, self.y)
			self.screen.blit(self.image, draw_pos)
		
			
		
		    
