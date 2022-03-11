import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


background = pygame.image.load("imgs/background.jpg")

run = True
while run:
	screen.blit(background, (0, 0))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
