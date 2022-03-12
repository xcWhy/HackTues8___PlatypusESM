import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
single_img = pygame.image.load('imgs_updated/Singleplayer.png').convert_alpha()
multi_img = pygame.image.load('imgs_updated/Multiplayer.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)
single = button.Button(50, 300, single_img, 700, 200)
multi = button.Button(780, 300, multi_img, 700, 200)

def quiz_func(new_start):
	if back.draw(screen):
		new_start = 0
	if single.draw(screen):
		print("Single player")
	if multi.draw(screen):
		print("Multiplayer")

	for event in pygame.event.get():

		if event.type == pygame.QUIT: exit()

	return new_start