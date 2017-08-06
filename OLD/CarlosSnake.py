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
food_list = pygame.sprite.Group()
tail_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

done = False

class Tail(pygame.sprite.Sprite):
	
	def __init__(self, x, y,largeur = 50):
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
			self.rect.x -= 50

	def moveRight(self):
		if not head.isAtWall():
			self.rect.x += 50

	def moveUp(self):
		if not head.isAtWall():
			self.rect.y -=50

	def moveDown(self):
		if not head.isAtWall():
			self.rect.y +=50

	def __str__(self):
		return "coord: (%d, %d)" % (self.rect.x, self.rect.y)

space = 10

#for i in range(0,5):
#	tail_list.add(Tail())
#	all_sprites_list.add(Tail())

head = Head()
food =Food()
food_list.add(food)
snake.append(head)
all_sprites_list.add(food)
all_sprites_list.add(head)

food.rect.x = random.randrange(SIZE[0])
food.rect.y = random.randrange(SIZE[1])

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_ESCAPE]:
		done = True
	elif keys[pygame.K_LEFT]:
		head.motionDirection = "left"
	elif keys[pygame.K_RIGHT]:
		head.motionDirection = "right"
	elif keys[pygame.K_UP]:
		head.motionDirection = "up"
	elif keys[pygame.K_DOWN]:
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

		tail = Tail(prevX, prevY)
		snake.append(tail)
		tail_list.add(tail)
		all_sprites_list.add(tail)

		print "snake head: ", snake[0]

		#head.tailLength+= 1

		"""
		if len(tail_list)== 0:
			tail = Tail(prevX, prevY)
			tail_list.add(tail)
			all_sprites_list.add(tail)
		else:
			for tail in tail_list:
		"""
		for s in all_sprites_list:
			if s == head:
				print "s coord x: ", s.rect.x
				print "s coord y: ", s.rect.y
				print "head coord x: ", head.rect.x
				print "head coord y: ", head.rect.y
		#print "head coord: ", all_sprites_list.head
		

		
		#print "list tail: ", len(tail_list)
		
	currentTailX = head.rect.x
	currentTailY = head.rect.y


	if head.motionDirection == "right":
		for tail in tail_list:
			tail.rect.x = currentTailX - tail.largeur - space
			currentTailX = currentTailX - tail.largeur - space
			tail.rect.y = currentTailY

	elif head.motionDirection == "left":
		for tail in tail_list:
			tail.rect.x = currentTailX + tail.largeur + space
			currentTailX += tail.largeur + space
			tail.rect.y = currentTailY
	elif head.motionDirection == "up":
		for tail in tail_list:
			tail.rect.y = currentTailY + tail.largeur + space
			currentTailY += tail.largeur + space
			tail.rect.x = head.rect.x
			#cutail.rect.y = head.rect.y + tail.largeur
	elif head.motionDirection == "down":
		for tail in tail_list:
			tail.rect.y = currentTailY - tail.largeur - space
			currentTailY = currentTailY - tail.largeur - space 
			tail.rect.x = head.rect.x
			#tail.rect.x = head.rect.x
			#tail.rect.y = head.rect.y - tail.largeur

	all_sprites_list.draw(screen)

	#pygame.display.update()
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(10)

pygame.quit()