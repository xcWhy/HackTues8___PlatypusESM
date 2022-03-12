import pygame
import pygame_textinput
import static
import button

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
share_bttn = pygame.image.load('imgs_updated/IfYouHavnetSeen.png').convert_alpha()
type_space = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)
share = static.Static(375, 50, share_bttn, 800, 200)
type = static.Static(375, 270, type_space, 800 ,500)

textinput = pygame_textinput.TextInputVisualizer()

base_font = pygame.font.Font('font/ChalkboardSE-Regular.ttf', 32)

def share_func(new_start):
	share.draw(screen)
	type.draw(screen)

	events = pygame.event.get()

	textinput.update(events)
	screen.blit(textinput.surface, (480, 375))

	if back.draw(screen):
		new_start = 0;

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	pygame.display.update()
	return new_start

