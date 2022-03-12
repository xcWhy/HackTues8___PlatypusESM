import pygame
import static
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

answer_1_prop = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
answer_2_prop = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
answer_3_prop = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
answer_4_prop = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
question_prop = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

back = button.Button(10, 690, back_bttn, 150, 100)
answer_1_button = button.Button(250, 300, answer_1_prop, 500, 200)
answer_2_button = button.Button(250, 500, answer_2_prop, 500, 200)
answer_3_button = button.Button(790, 300, answer_3_prop, 500, 200)
answer_4_button = button.Button(790, 500, answer_4_prop, 500, 200)
question_static = static.Static(235, 10, question_prop, 1065, 250)

def single_player_func(new_start):
	screen.blit(background, (0, 0))

	if back.draw(screen):
		new_start = 3

	question_static.draw(screen)

	if answer_1_button.draw(screen):
		print("Answer 1")
	if answer_2_button.draw(screen):
		print("Answer 2")
	if answer_3_button.draw(screen):
		print("Answer 3")
	if answer_4_button.draw(screen):
		print("Answer 4")

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

	return new_start