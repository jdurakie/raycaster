"""
Contains code to render images with PyGame
"""

import pygame, sys
from pygame.locals import *

class ImageRenderer(object):
	def __init__(self, size, display_size = (600, 600)):

		self.display_size = display_size
		self.screen = pygame.display.set_mode(display_size, HWSURFACE|DOUBLEBUF|RESIZABLE)
		self.render = pygame.Surface((size))
		self.image = None

	def point(self, location, color=(255, 0, 0)):
		if self.image == None:
			self.image = pygame.PixelArray(self.render)
		self.image[location[0]][location[1]] = color

	def saveImage(self, _):
		del self.image
		self.image = None
		transformed = pygame.transform.scale(self.render, self.display_size)
		self.screen.blit(transformed, (0, 0))
		pygame.display.flip()
