#je fais un test de git mon grand

import pygame
import random
import os

x = 100
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

SIZE = (1200,800)
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [0,255,0]
BLUE = [0,0,255]


FONT_40 = pygame.font.Font("Data/space_invaders.ttf", 40)
FONT_20 = pygame.font.Font("Data/space_invaders.ttf", 20)
FONT_10 = pygame.font.Font("Data/space_invaders.ttf", 10)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("head Carlos")

#food_list = pygame.sprite.Group()
#all_sprites_list = pygame.sprite.Group()

spaceBetweenCells = 10

DIMENSION_CELL = 50
STEP = DIMENSION_CELL
#direction = None

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

	def __init__(self, startX = 150, startY = 150, direction = "right"):
		self.coord = []
		self.sprite_snake_list = pygame.sprite.Group()
		self.startX = startX
		self.startY = startY
		self.head = Cell(self.startX, self.startY)
		self.coord.append(self.head)
		#self.sprite_snake_list = pygame.sprite.Group()
		#self.sprite_snake_list.add(self.head)
		#all_sprites_list.add(self.head)
		self.direction = direction
		self.step = DIMENSION_CELL
		self.spaceBetweenCells = 10
		self.score = 0
		self.previousTail = None

	def explose(self, message):
		boom = FONT_40.render(message, True, WHITE)
		#screen.blit(theScoreP1, 50, 5)
		screen.blit(boom, (SIZE[0]/2, SIZE[1]/2))
		self.killSnake()

	def killSnake(self):
		for cell in self.coord:
			cell.kill()
		
	def grow(self, allSpritesList):
		newCell = Cell(self.previousTail[0], self.previousTail[1])
		self.coord.append(newCell)
		self.sprite_snake_list.add(newCell)
		allSpritesList.add(newCell)
		

	def createTail(self, longueur):
		tmp = self.startX
		for i in range (0,longueur):
			cell = Cell(tmp- DIMENSION_CELL - self.spaceBetweenCells, self.startY)
			tmp = tmp - DIMENSION_CELL - self.spaceBetweenCells
			self.coord.append(cell)
			self.sprite_snake_list.add(cell)
			#all_sprites_list.add(cell)
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

	def setNewPos(self, snake_coord):
		coordFoodValid = False
		while not coordFoodValid:
			self.rect.x = random.randrange(SIZE[0] - self.largeur)
			self.rect.y = random.randrange(SIZE[1] - self.largeur)
			coordTmp = self.rect.x, self.rect.y
			if coordTmp not in snake_coord:
				coordFoodValid = True

class App(object):
	
	def __init__(self):
		self.allDone = False
		self.gameDone = False
		self.snake = Snake()
		self.food = Food()
		self.food_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()
		self.credits = 0
	

	def reInitEverything(self):
		self.__init__()
		"""
		self.allDone = False
		self.gameDone = False
		self.snake = None
		self.snake = Snake()
		self.food = Food()
		self.food_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()
		"""
	def initEverything(self):
		
		self.snake.createTail(3)
		self.food.rect.x = random.randrange(SIZE[0])
		self.food.rect.y = random.randrange(SIZE[1])
		self.food_list.add(self.food)
		self.all_sprites_list.add(self.food)
		self.all_sprites_list.add(self.snake.head)
		for cell in self.snake.coord:
			self.all_sprites_list.add(cell)

	def showStartScreen(self):
		screen.fill(BLACK)
		insertCoin = FONT_20.render("insert coin (PRESS 5)", True, WHITE)
		snake = FONT_40.render("SNAKE!!!", True, GREEN)
		credits = FONT_20.render("Credits:", True, WHITE)
		numberCredits = FONT_20.render(str(self.credits), True, WHITE)
		pressStart = FONT_20.render("Press Start! (1)", True, WHITE)
		screen.blit(credits, (SIZE[0]-250,SIZE[1]-30))
		screen.blit(numberCredits, (SIZE[0]-130, SIZE[1] -30))
		screen.blit(snake, ((SIZE[0] - 150)/2 , SIZE[1]/4))
		if self.credits <1:
			screen.blit(insertCoin,((SIZE[0]- 220)/2, SIZE[1]*3/5) )
		else:
			screen.blit(pressStart, ((SIZE[0]- 220)/2, SIZE[1]*3/5))
		pygame.display.flip()


	def mainLoop(self):
		print "start main loop"
		#screen.fill(BLACK)
		self.gameDone = False
		"""
		while not self.allDone:
			print "Voulez-vous jouer une autre partie"
			reponse = raw_input()
			if reponse == "y":
				self.reInitEverything()
			else:
				#allDone = True
				break
		"""

		self.initEverything()
		while not self.gameDone:

			screen.fill(BLACK)
			print "main loop screen"

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#self.allDone = True
					self.gameDone = True

			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				self.allDone = True
				self.gameDone = True
				return gameDone
			elif keys[pygame.K_LEFT] and self.snake.direction != "right":
				self.snake.direction = "left"
			elif keys[pygame.K_RIGHT] and self.snake.direction != "left":
				self.snake.direction = "right"
			elif keys[pygame.K_UP] and self.snake.direction != "down":
				self.snake.direction = "up"
			elif keys[pygame.K_DOWN] and self.snake.direction != "up":
				self.snake.direction = "down"
			elif keys[pygame.K_5]:
				print "=========================="
				print len(self.snake.coord)

			if pygame.sprite.spritecollide(self.snake.coord[0], self.snake.sprite_snake_list, False):
				print"boom in snake!"
				self.snake.explose("Boom in snake!!!")
				self.gameDone = True
				return self.gameDone

			if self.snake.isAtWall():
				self.snake.explose("Boom in Wall!!!")
				print "head of snake coord: ", self.snake.head
				#del self.snake
				self.snake.head = Cell(150,150)
				print"boom in wall!"
				self.gameDone = True
				return self.gameDone
				
			else:
				self.snake.update()		
			
			if pygame.sprite.spritecollide(self.snake.coord[0], self.food_list, False):
				self.snake.grow(self.all_sprites_list)
				self.food.setNewPos(self.snake.coord)
				print "lenght of snake: ", len(self.snake.coord)
				self.snake.score += 10
			
			self.all_sprites_list.draw(screen)

			theScoreP1 = FONT_40.render(str(self.snake.score), True, WHITE)
			
			screen.blit(theScoreP1, (SIZE[0] - DIMENSION_CELL*1.5 , 10))
			pygame.display.flip()
			print "end of main loop"

			# Limit to 60 frames per second
			clock.tick(10)

		#pygame.quit()


if __name__ == '__main__':
    app = App()

    toutFini = False
    
    while not toutFini:
    	app.showStartScreen()
    	keys = pygame.key.get_pressed()
    	if keys[pygame.K_ESCAPE]:
    		toutFini = True
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			toutFini = True
    		if event.type == pygame.KEYDOWN:
	    		if event.key == pygame.K_5:
	    			app.credits= app.credits + 1
	    			print "pressed 5"
	    		elif event.key == pygame.K_1 and app.credits>0:
	    			print "pressed 1"
	    			app.mainLoop()


    pygame.quit()	

#allDone = False

#snake = Snake() 
#snake.createTail()

#food = Food()
#food.rect.x = random.randrange(SIZE[0])
#food.rect.y = random.randrange(SIZE[1])

#food_list.add(food)
#all_sprites_list.add(food)

"""

while not allDone:

	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			allDone = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		allDone = True
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

"""