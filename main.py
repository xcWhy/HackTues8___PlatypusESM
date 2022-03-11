import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_img = pygame.image.load('imgs/button_assets.png').convert_alpha()

button_1 = button.Button(450, -50, start_img)
button_2 = button.Button(450, 100, start_img)
button_3 = button.Button(450, 250, start_img)
button_4 = button.Button(450, 400, start_img)

background = pygame.image.load("imgs/background.jpg")

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

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()