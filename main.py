from character import character_func
from training import training_func
from quiz import quiz_func
from Share import share_func
import pygame
import static
import button
global new_start

new_start = 0

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

button_character = pygame.image.load('imgs_updated/Character.png').convert_alpha()
button_training = pygame.image.load('imgs_updated/TrainingWheels.png').convert_alpha()
button_game = pygame.image.load('imgs_updated/OutInTheSpace.png').convert_alpha()
button_share = pygame.image.load('imgs_updated/ShareYourKnowledge.png').convert_alpha()

button_1 = button.Button(575, 100, button_character, 400, 100)
button_2 = button.Button(575, 250, button_training, 400, 100)
button_3 = button.Button(575, 400, button_game, 400, 100)
button_4 = button.Button(575, 550, button_share, 400, 100)

def main_func():
	global new_start
	if button_1.draw(screen):
		new_start = 1
	if button_2.draw(screen):
		new_start = 2
	if button_3.draw(screen):
		new_start = 3
	if button_4.draw(screen):
		new_start = 4

while True:
	screen.blit(background, (0, 0))

	if new_start == 0:
		main_func()
	elif new_start == 1:
		new_start = character_func(new_start)
	elif new_start == 2:
		new_start = training_func(new_start)
	elif new_start == 3:
		new_start = quiz_func(new_start)
	elif new_start == 4:
		new_start = share_func(new_start)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: exit()

	pygame.display.update()

pygame.quit()