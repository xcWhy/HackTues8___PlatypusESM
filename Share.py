import pygame
import static
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs/Back.png').convert_alpha()

back_button = button.Button(-100, -90, back_bttn, 350, 350)

run = True
while run:
	screen.blit(background, (0, 0))

	if back_button.draw(screen):
		print("Back")

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
