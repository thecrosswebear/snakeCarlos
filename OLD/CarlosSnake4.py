#je fais un test de git mon grand

import pygame
import random

pygame.init()

SIZE = (1200,800)
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [0,255,0]
BLUE = [0,0,255]


FONT = pygame.font.Font("Data/space_invaders.ttf", 40)
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
		return "\tcell (%d,%d)\n"% (self.rect.x, self.rect.y)

class Snake (object):

	def __init__(self, startX = 150, startY= 150, direction = "right"):
		self.coord = []
		self.sprite_snake_list = pygame.sprite.Group()
		self.startX = startX
		self.startY = startY
		self.head = Cell(self.startX, self.startY)
		self.coord.append(self.head)
		#self.sprite_snake_list.add(self.head)
		all_sprites_list.add(self.head)
		self.direction = direction
		self.step = DIMENSION_CELL
		self.spaceBetweenCells = 10
		self.score = 0
		self.previousTail = None

	def explose(self, message):
		boom = FONT.render(message, True, WHITE)
		#screen.blit(theScoreP1, 50, 5)
		screen.blit(boom, (SIZE[0]/2, SIZE[1]/2))
		self.killSnake()

	def killSnake(self):
		for cell in self.coord:
			cell.kill()
		#for cell in self.sprite_snake_list:
		#	cell.kill()
		#self.head.kill()

	def createTail(self):
		tmp = self.startX
		for i in range (0,7):
			cell = Cell(tmp- DIMENSION_CELL - self.spaceBetweenCells, self.startY)
			tmp = tmp - DIMENSION_CELL - self.spaceBetweenCells
			self.coord.append(cell)
			self.sprite_snake_list.add(cell)
			all_sprites_list.add(cell)
		#print self

	
	def isAtWall(self):
		if self.head.rect.x >= SIZE[0]:
			self.head.rect.x = SIZE[0] - self.step
			return True
		elif self.head.rect.x < 0:
			self.head.rect.x = 0
			return True
		elif self.head.rect.y >= SIZE[1]:
			self.head.rect.y = SIZE[1] - self.step
			return True
		elif self.head.rect.y < 0:
			self.head.rect.y = 0
			return True
		else:
			return False

	def update(self):

		#if not self.isAtWall():
		# update previous positions
			#self.previousTail = Cell(self.coord[len(self.coord) -1].rect.x, self.coord[len(self.coord) -1].rect.y) 
		self.previousTail = (self.coord[len(self.coord) -1].rect.x, self.coord[len(self.coord) -1].rect.y)  
		for i in range(len(self.coord)-1,0,-1):
			self.coord[i].rect.x = self.coord[i-1].rect.x
			self.coord[i].rect.y = self.coord[i-1].rect.y     	
           	
	# update position of head of snake
 		if self.direction == "left":
 			self.coord[0].rect.x = self.coord[0].rect.x - self.step - self.spaceBetweenCells
 		if self.direction == "right":
 			self.coord[0].rect.x = self.coord[0].rect.x + self.step + self.spaceBetweenCells
 		if self.direction == "down":
 			self.coord[0].rect.y = self.coord[0].rect.y + self.step + self.spaceBetweenCells
 		if self.direction == "up":
 			self.coord[0].rect.y = self.coord[0].rect.y - self.step - self.spaceBetweenCells
		
 	def __str__(self):
 		tmp = ""
 		for i in range(0,len(self.coord)-1):
 			print self.coord[i]
 		return tmp


class Food(pygame.sprite.Sprite):

	def __init__(self, largeur = 30):
		super(Food, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur,largeur])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.score = 0

class App(object):
	pass



done = False

snake = Snake() 
snake.createTail()

food = Food()
food.rect.x = random.randrange(SIZE[0])
food.rect.y = random.randrange(SIZE[1])

food_list.add(food)
all_sprites_list.add(food)

while not done:

	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	elif keys[pygame.K_LEFT] and snake.direction != "right":
		snake.direction = "left"
	elif keys[pygame.K_RIGHT] and snake.direction != "left":
		snake.direction = "right"
	elif keys[pygame.K_UP] and snake.direction != "down":
		snake.direction = "up"
	elif keys[pygame.K_DOWN] and snake.direction != "up":
		snake.direction = "down"
	elif keys[pygame.K_5]:
		print "=========================="
		print len(snake.coord)
		

	if pygame.sprite.spritecollide(snake.coord[0], snake.sprite_snake_list, False):
		print"boom in snake!"
		snake.explose("Boom in snake!!!")

	if snake.isAtWall():
		snake.explose("Boom in Wall!!!")
		print"boom in wall!"
		
	else:
		snake.update()
	
	if pygame.sprite.spritecollide(snake.coord[0], food_list, False):
		coordFoodValid = False
		print "lenght of snake: ", len(snake.coord)
		newCell = Cell(snake.previousTail[0], snake.previousTail[1])
		snake.coord.append(newCell)
		snake.sprite_snake_list.add(newCell)
		all_sprites_list.add(newCell)
		while not coordFoodValid:
			food.rect.x = random.randrange(SIZE[0] - food.largeur)
			food.rect.y = random.randrange(SIZE[1] - food.largeur)
			coordTmp = food.rect.x, food.rect.y
			if coordTmp not in snake.coord:
				coordFoodValid = True
		snake.score += 10

	all_sprites_list.draw(screen)

	theScoreP1 = FONT.render(str(snake.score), True, WHITE)
	
	screen.blit(theScoreP1, (SIZE[0] - DIMENSION_CELL*1.5 , 10))
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(10)

pygame.quit()