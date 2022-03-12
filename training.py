import pygame
import static
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535
WHITE = 0, 0, 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw(text, X, Y):
	pygame.init()
	font = pygame.font.SysFont('Comic Sans MS', 80)
	paragraph = font.render(text, True, WHITE)
	display_surface.blit(paragraph, (X, Y))



back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
question = pygame.image.load('imgs_updated/FlashCard_Template.png').convert_alpha()
answer = pygame.image.load('imgs_updated/FlashCard_Template.png').convert_alpha()
reverse = pygame.image.load('imgs_updated/UnoReverse.png').convert_alpha()
next = pygame.image.load('imgs_updated/Next.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)
question_static = static.Static(450, 150, question, 650, 600)
answer_static = static.Static(450, 150, answer, 650, 600)
reverse_button = button.Button(615, 550, reverse, 100, 100)
next_button = button.Button(750, 550, next, 150, 100)

def training_func(new_start):
	flip = False

	question_static.draw(screen)
	while new_start == 2:

		if reverse_button.draw(screen):
			if flip == False:
				flip = True
			else:
				flip = False

			if flip:
				answer_static.draw(screen)
				draw("vypros edno", 550, 350)
			else:
				question_static.draw(screen)

		if back.draw(screen):
			new_start = 0

		if next_button.draw(screen):
			print("Next")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		pygame.display.update()

	return new_start