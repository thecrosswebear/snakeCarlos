import pygame
import random

pygame.init()

SIZE = (800,800)
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [0,255,0]
BLUE = [0,0,255]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("head Carlos")

positions = []
food_list = pygame.sprite.Group()
tail_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

spaceBetweenCells = 10

DIMENSION_CELL = 50
STEP = DIMENSION_CELL
direction = None

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
		print "\tcell (%d,%d)"% (self.rect.x, self.rect.y)

class Snake (object):

	def __init__(self, startX = 150, startY= 150):
		self.coord = []
		self.sprite_snake_list = pygame.sprite.Group()
		self.startX = startX
		self.startY = startY
		self.head = Cell(self.startX, self.startY)
		self.coord.append(head)
		self.sprite_snake_list.add(head)
		all_sprites_list.add(head)
		self.direction = None
		self.step = DIMENSION_CELL
		self.spaceBetweenCells = 10
	
	def createTail(self):
		tmp = self.startX
		for i in range (0,4):
			cell = Cell(tmp- DIMENSION_CELL - self.spaceBetweenCells, startY)
			tmp = tmp - DIMENSION_CELL - self.spaceBetweenCells
			snake.append(cell)
		all_sprites_list.add(cell)


	def update(self):
		pass

class Food(pygame.sprite.Sprite):

	def __init__(self, largeur = 30):
		super(Food, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur,largeur])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.score = 0

done = False

snake = []
startX =350
startY = 150

head = Cell(startX,startY)
snake.append(head)
all_sprites_list.add(head)

#creation du corps du serpent
for i in range (0,4):
	cell = Cell(startX- DIMENSION_CELL - spaceBetweenCells, startY)
	startX = startX - DIMENSION_CELL - spaceBetweenCells
	snake.append(cell)
	all_sprites_list.add(cell)

def update():
# update previous positions
    for i in range(len(snake)-1,0,-1):
        #print "self.x[" + str(i) + "] = self.x[" + str(i-1) + "]"
        snake[i].rect.x = snake[i-1].rect.x
        snake[i].rect.y = snake[i-1].rect.y
        
    # update position of head of snake
    if direction == "left":
        snake[0].rect.x = snake[0].rect.x - STEP - spaceBetweenCells
    if direction == "right":
        snake[0].rect.x = snake[0].rect.x + STEP + spaceBetweenCells
    if direction == "down":
        snake[0].rect.y = snake[0].rect.y + STEP + spaceBetweenCells
    if direction == "up":
        snake[0].rect.y = snake[0].rect.y - STEP - spaceBetweenCells
    
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	elif keys[pygame.K_LEFT] and direction != "right":
		direction = "left"
	elif keys[pygame.K_RIGHT] and direction != "left":
		direction = "right"
	elif keys[pygame.K_UP] and direction != "down":
		direction = "up"
	elif keys[pygame.K_DOWN] and direction != "up":
		direction = "down"

	update()

	screen.fill(BLACK)
	all_sprites_list.draw(screen)

	#pygame.display.update()
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(10)


	#print snake[0].rect.x
	#print snake[0].rect.y

pygame.quit()