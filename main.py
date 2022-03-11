import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.jpg")

button_character = pygame.image.load('imgs/Character.png').convert_alpha()
button_training = pygame.image.load('imgs/TrainingWheels.png').convert_alpha()
button_game = pygame.image.load('imgs/OutInTheSpace.png').convert_alpha()
button_share = pygame.image.load('imgs/ShareYourKnowledge.png').convert_alpha()

button_1 = button.Button(500, 0, button_character, 500, 450)
button_2 = button.Button(500, 150, button_training, 500, 450)
button_3 = button.Button(500, 300, button_game, 500, 450)
button_4 = button.Button(500, 450, button_share, 500, 450)

run = True
while run:
	screen.blit(background, (0, 0))

	if button_1.draw(screen):
		print('Button 1')
	if button_2.draw(screen):
		print('Button 2')
	if button_3.draw(screen):
		print('Button 3')
	if button_4.draw(screen):
		print('Button 4')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()