import Constants
import pygame
pygame.init()


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
		#for cell in self.coord:
		#	cell.kill()
		for cell in self.sprite_snake_list:
			cell.kill()
		self.head.kill()



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