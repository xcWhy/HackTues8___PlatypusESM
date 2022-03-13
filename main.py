from screen_info import screen
from settings import settings_func
from homepg import homepage_func
from character import character_func
from training import training_func
from quiz import quiz_func
from single_player import single_player_func
from Share import share_func
from text import draw
import pygame
import static
import button
global new_start

background = pygame.image.load("imgs/background.png")

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

button_1 = button.Button(575, 100, bttn, 400, 100)
button_2 = button.Button(575, 250, bttn, 400, 100)
button_3 = button.Button(575, 400, bttn, 400, 100)
button_4 = button.Button(575, 550, bttn, 400, 100)
back = button.Button(700, 675, bttn, 155, 100)

new_start = -1

def main_func():
	global new_start

	if back.draw(screen):
		new_start = -1
	if button_1.draw(screen):
		new_start = 1
	if button_2.draw(screen):
		new_start = 2
	if button_3.draw(screen):
		new_start = 3
	if button_4.draw(screen):
		new_start = 4

	draw("Character", 700, 125, 36)
	draw("Training Wheels", 640, 275, 36)
	draw("Out in the space", 635, 425, 36)
	draw("Share your knowledge", 605, 575, 34)
	draw("Back", 740, 700, 36)


while True:
	screen.blit(background, (0, 0))

	if new_start == -2:
		new_start = settings_func(new_start)
	if new_start == -1:
		new_start = homepage_func(new_start)
	elif new_start == 0:
		main_func()
	elif new_start == 1:
		new_start = character_func(new_start)
	elif new_start == 2:
		new_start = training_func(new_start)
	elif new_start == 3:
		new_start = quiz_func(new_start)
	elif new_start == 4:
		new_start = share_func(new_start)
	elif new_start == 5:
		new_start = single_player_func(new_start)

	for event in pygame.event.get():
		if event.type == pygame.QUIT: exit()

	pygame.display.update()

pygame.quit()