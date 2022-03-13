from screen_info import screen
from text import draw
import pygame
import button

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

back = button.Button(10, 10, bttn, 150, 100)
single = button.Button(50, 300, bttn, 700, 200)
multi = button.Button(780, 300, bttn, 700, 200)

def quiz_func(new_start):

	if back.draw(screen):
		new_start = 0
	if single.draw(screen):
		new_start = 5
	if multi.draw(screen):
		new_start = 6

	draw("Back", 45, 35, 36)
	draw("Singleplayer", 250, 365, 50)
	draw("Multiplayer", 1000, 365, 50)

	for event in pygame.event.get():

		if event.type == pygame.QUIT: exit()

	return new_start