from Constants import *
import pygame
pygame.init()

class Cell(pygame.sprite.Sprite):

	def __init__(self, x, y, largeur = DIMENSION_CELL):
		super(Cell, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur, largeur])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def __str__(self):
		return "\tcell (%d,%d)\n"% (self.rect.x, self.rect.y)