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

snake = []
positions = []
food_list = pygame.sprite.Group()
tail_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

spaceBetweenCells = 10

DIMENSION_CELL = 50
STEP = DIMENSION_CELL

done = False

class Cell(pygame.sprite.Sprite):

	def __init__(self, x, y, largeur = DIMENSION_CELL):
		super(Cell, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur, largeur])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


class Snake(object):
	
	def __init__(self):
		serpent = []


class Tail(pygame.sprite.Sprite):
	
	def __init__(self, x, y,largeur = DIMENSION_CELL):
		super(Tail, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur, largeur])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def move(self):
		pass

class Food(pygame.sprite.Sprite):

	def __init__(self, largeur = 30):
		super(Food, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur,largeur])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.score = 0

class Head(pygame.sprite.Sprite):

	def __init__(self, largeur = 50):
		super(Head,self).__init__()
		self.largeur = largeur
		self.xCoord = 150
		self.yCoord = 150
		self.deplacement = 50
		self.image = pygame.Surface([largeur, largeur])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.motionDirection = None
		#self.tailLength = 0

	def isAtWall(self):
		if self.rect.x >= SIZE[0]:
			self.rect.x = SIZE[0] - self.largeur
			return True
		elif self.rect.x < 0:
			self.rect.x = 0
			return True
		elif self.rect.y >= SIZE[1]:
			self.rect.y = SIZE[1] - self.largeur
			return True
		elif self.rect.y < 0:
			self.rect.y = 0
			return True
		else:
			return False

	def move(self):

		if self.motionDirection == "left":
			self.moveLeft()
		elif self.motionDirection == "right":
			self.moveRight()
		elif self.motionDirection == "down":
			self.moveDown()
		elif self.motionDirection == "up":
			self.moveUp()

	def moveLeft(self):
		if not head.isAtWall():
			self.rect.x -= STEP

	def moveRight(self):
		if not head.isAtWall():
			self.rect.x += STEP

	def moveUp(self):
		if not head.isAtWall():
			self.rect.y -=STEP

	def moveDown(self):
		if not head.isAtWall():
			self.rect.y +=STEP

	def __str__(self):
		return "coord: (%d, %d)" % (self.rect.x, self.rect.y)



#for i in range(0,5):
#	tail_list.add(Tail())
#	all_sprites_list.add(Tail())

head = Head()
positions.append((head.rect.x,head.rect.y))
food =Food()
food_list.add(food)
snake.append(head)
all_sprites_list.add(food)
all_sprites_list.add(head)

food.rect.x = random.randrange(SIZE[0])
food.rect.y = random.randrange(SIZE[1])

def movePositions(newHead, positions):
	positions[0] = newHead
	for i in range (0, len(positions) -2):
		positions[i +1] = positions[i]

def printPositions(positions):
	print "Tableau: ",
	for i in range(0, len(positions) -1):
		print"(", positions[i],

	print ")"



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_ESCAPE]:
		done = True
	elif keys[pygame.K_LEFT] and head.motionDirection != "right":
		head.motionDirection = "left"
	elif keys[pygame.K_RIGHT] and head.motionDirection != "left":
		head.motionDirection = "right"
	elif keys[pygame.K_UP] and head.motionDirection != "down":
		head.motionDirection = "up"
	elif keys[pygame.K_DOWN] and head.motionDirection != "up":
		head.motionDirection = "down"
	
	prevX = head.rect.x
	prevY = head.rect.y	
	#print "prevHead: ", prevHead
	head.move()	
	
	#print "currenthead: ", head
	screen.fill(BLACK)
	
	if pygame.sprite.spritecollide(head, food_list, False):
		food.rect.x = random.randrange(SIZE[0] - food.largeur)
		food.rect.y = random.randrange(SIZE[1] - food.largeur)

		if len(positions)== 1:
			tail = Tail(prevX, prevY)
			positions.append((tail.rect.x, tail.rect.y))
			snake.append(tail)
			tail_list.add(tail)
			all_sprites_list.add(tail)

	movePositions(head.rect, positions)
	printPositions(positions)

	"""
	tail = Tail(prevX, prevY)
	snake.append(tail)
	tail_list.add(tail)
	all_sprites_list.add(tail)
	"""
	

	#head.tailLength+= 1

	"""
	
	else:
		for tail in tail_list:
			snake[]
	for s in all_sprites_list:
		if s == head:
			print "s coord x: ", s.rect.x
			print "s coord y: ", s.rect.y
			print "head coord x: ", head.rect.x
			print "head coord y: ", head.rect.y
	#print "head coord: ", all_sprites_list.head
	
	"""
	
	#print "list tail: ", len(tail_list)
		
	currentTailX = head.rect.x
	currentTailY = head.rect.y

	newTailTest = Tail(189,55)
	newTailTest.rect = 44,44

	#print "lenght de tail", len(tail_list)

	if head.motionDirection == "right":
		for tail in tail_list:
			tail.rect.x = currentTailX - tail.largeur - spaceBetweenCells
			currentTailX = currentTailX - tail.largeur - spaceBetweenCells
			tail.rect.y = currentTailY

	elif head.motionDirection == "left":
		for tail in tail_list:
			tail.rect.x = currentTailX + tail.largeur + spaceBetweenCells
			currentTailX += tail.largeur + spaceBetweenCells
			tail.rect.y = currentTailY
	elif head.motionDirection == "up":
		for tail in tail_list:
			tail.rect.y = currentTailY + tail.largeur + spaceBetweenCells
			currentTailY += tail.largeur + spaceBetweenCells
			tail.rect.x = head.rect.x
			#cutail.rect.y = head.rect.y + tail.largeur
	elif head.motionDirection == "down":
		for tail in tail_list:
			tail.rect.y = currentTailY - tail.largeur - spaceBetweenCells
			currentTailY = currentTailY - tail.largeur - spaceBetweenCells 
			tail.rect.x = head.rect.x
			#tail.rect.x = head.rect.x
			#tail.rect.y = head.rect.y - tail.largeur

	all_sprites_list.draw(screen)

	#pygame.display.update()
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(10)

pygame.quit()