import pygame
import static
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
question = pygame.image.load('imgs/karta_vyp.png').convert_alpha()
answer = pygame.image.load('imgs/karta_otg.png').convert_alpha()
arrow = pygame.image.load('imgs/ButtonArrow.png').convert_alpha()
next = pygame.image.load('imgs/Next.png').convert_alpha()

back_button = button.Button(10, 10, back_bttn, 150, 100)
question_static = static.Static(450, 150, question, 650, 600)
answer_static = static.Static(450, 150, answer, 650, 600)
arrow_button = button.Button(75, 300, arrow, 1200, 1200)
next_button = button.Button(600, 430, next, 400, 410)

run = True
while run:
	screen.blit(background, (0, 0))

	switch_file = 0

	if back_button.draw(screen):
		switch_file = 1
		break

	if arrow_button.draw(screen):
		answer_static.draw(screen)
	else:
		question_static.draw(screen)

	if next_button.draw(screen):
		print("Next")


	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

if switch_file == 1:
	import main

pygame.quit()
