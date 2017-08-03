import pygame

pygame.init()

SIZE =(800,800)
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [0,255,0]
BLUE = [0,0,255]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("calice de snake")

done = False

snake = pygame.sprite.Group()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Cell(pygame.sprite.Sprite):

	deplacement = 50
	space = 10
	
	def __init__(self, x=350, y=150, largeur=50):
		super(Cell, self).__init__()
		self.largeur = largeur
		self.image = pygame.Surface([largeur, largeur])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.motionDirection = None

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

	def move(self, direction):
		pass

	def move(self):

		if self.motionDirection == "l":
			self.moveLeft()
		elif self.motionDirection == "r":
			self.moveRight()
		elif self.motionDirection == "d":
			self.moveDown()
		elif self.motionDirection == "u":
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

head = Cell()
snake.add(head)

tmpx = head.rect.x
tmpy = head.rect.y
for i in range(0,5):
	cell = Cell(tmpx - head.largeur - head.space)
	snake.add(Cell())
	tmpx = tmpx - head.largeur
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	elif keys[pygame.K_LEFT]:
		head.motionDirection = "l"
	elif keys[pygame.K_RIGHT]:
		head.motionDirection = "r"
	elif keys[pygame.K_DOWN]:
		head.motionDirection = "d"
	elif keys[pygame.K_UP]:
		head.motionDirection ="u"

	head.move()
	screen.fill(BLACK)
	#pygame.draw.rect(screen, GREEN, (50,50,50,50))

	snake.draw(screen)
	
	#pygame.display.update()
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(10)
	

pygame.quit()