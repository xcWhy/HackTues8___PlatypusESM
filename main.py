import pygame
import button

switch_file = 0

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

button_character = pygame.image.load('imgs_updated/Character.png').convert_alpha()
button_training = pygame.image.load('imgs_updated/TrainingWheels.png').convert_alpha()
button_game = pygame.image.load('imgs_updated/Character.png').convert_alpha()
button_share = pygame.image.load('imgs_updated/Character.png').convert_alpha()

button_1 = button.Button(575, 100, button_character, 400, 100)
button_2 = button.Button(575, 250, button_training, 400, 100)
button_3 = button.Button(575, 400, button_game, 400, 100)
button_4 = button.Button(575, 550, button_share, 400, 100)

run = True
while run:
	screen.blit(background, (0, 0))

	if button_1.draw(screen):
		print("1")
		switch_file = 1
		break
	if button_2.draw(screen):
		print("2")
		switch_file = 2
		break
	if button_3.draw(screen):
		print("3")
		switch_file = 3
		break
	if button_4.draw(screen):
		print("4")
		switch_file = 4
		break

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

#if switch_file == 1:

if switch_file == 2:
	import training
#if switch_file == 3:

#if switch_file == 4:

pygame.quit()