import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
single_img = pygame.image.load('imgs_updated/Singleplayer.png').convert_alpha()
multi_img = pygame.image.load('imgs_updated/Multiplayer.png').convert_alpha()

back_button = button.Button(10, 10, back_bttn, 150, 100)
single = button.Button(50, 300, single_img, 700, 300)
multi = button.Button(780, 300, multi_img, 700, 300)

run = True
while run:
	screen.blit(background, (0, 0))

	switch_file = 0

	if single.draw(screen):
		print("drun")
	if multi.draw(screen):
		print("drun drun")

	if back_button.draw(screen):
		switch_file = 1
		break

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

if switch_file == 1:
	import main

pygame.quit()