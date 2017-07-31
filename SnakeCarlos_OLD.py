import pygame

from pygame.locals import *
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello, World!")




class Snake(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super(Snake, self).__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]


def main():
	
	x, y = 0, 0
	move_x, move_y = 0, 0

	all_sprites_list = pygame.sprite.Group()
	snake = Snake()

	all_sprites_list.add(snake)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					print "keyleft"
					move_x = -1
				elif event.key == K_RIGHT:
					move_x = +1
				elif event.key == K_UP:
					move_y = -1
				elif event.key == K_DOWN:
					move_y = +1
			elif event.type == KEYUP:
				if event.key == K_LEFT:
					move_x = 0
				elif event.key == K_RIGHT:
					move_x = 0
				elif event.key == K_UP:
					move_y = 0
				elif event.key == K_DOWN:
					move_y = 0
		
		x+= move_x
		y+= move_y
		#print "Position souris: " , pygame.mouse.get_pos()

		all_sprites_list.draw(screen)
		
		pygame.display.flip()

if __name__ == "__main__":
	main()


#background = pygame.image.load(background_image_filename).convert()
#mouse_cursor = pygame.image.load(mouse_image_filename)


