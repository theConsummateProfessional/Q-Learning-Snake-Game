#class imports
from classes.food import Food
from classes.body import Body
from classes.snake import Snake

#regular imports
import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
win_width = 500
win_height = 500

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")
bigRun = True

while bigRun:
	size = 10
	xFood = random.randrange(60, 500, 10)
	yFood = random.randrange(60, 500, 10)
	xHeadSnake = random.randrange(60, 500, 10)
	yHeadSnake = random.randrange(60, 500, 10)
	food = Food(xFood, yFood, size, size)
	snake = Snake(xHeadSnake, yHeadSnake)
	length_of_body = 1
	x_change = 0
	y_change = 0
	clock = pygame.time.Clock()

	run = True

	def draw_snake(snake, size):
		for node in snake.bodyNodes:
			pygame.draw.rect(win, white, (node.x, node.y, size, size))

	def draw_text(text, size, color, bold, italic):
		font = pygame.font.SysFont("Serif Gothic", size, bold, italic)
		text = font.render(text, True, color)
		return text

	while run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				bigRun = False

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			x_change = -size
			y_change = 0

		elif keys[pygame.K_RIGHT]:
			x_change = size
			y_change = 0

		elif keys[pygame.K_UP]:
			x_change = 0
			y_change = -size

		elif keys[pygame.K_DOWN]:
			x_change = 0
			y_change = size


		xHeadSnake += x_change
		yHeadSnake += y_change

		win.fill(black)

		pygame.draw.rect(win, red, (food.x, food.y, size, size))

		snake.headX = xHeadSnake
		snake.headY = yHeadSnake
		body = Body(xHeadSnake, yHeadSnake, size, size)
		snake.bodyNodes.append(body)

		if len(snake.bodyNodes) > length_of_body:
			del snake.bodyNodes[0]

		for segment in snake.bodyNodes [:-1]:
			if ((segment.x == snake.headX) and (segment.y == snake.headY)):
				run = False

		if((snake.headX > 500 or snake.headX < 0) or (snake.headY > 500 or snake.headY < 60)):
			run = False

		draw_snake(snake, size)

		score = draw_text("Score: " + str(length_of_body - 1), 50, white, True, False)
		win.blit(score, (0, 0))
		pygame.draw.line(win, white, (0, 60), (500,60), 1)

		pygame.display.update()

		if xHeadSnake == food.x and yHeadSnake == food.y:
			xFood = random.randrange(0, 500, 10)
			yFood = random.randrange(60, 500, 10)
			food.changePos(xFood, yFood)
			length_of_body += 1

		clock.tick(10)



