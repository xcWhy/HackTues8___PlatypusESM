import pygame
import static
import button

from PIL import Image, ImageFont, ImageDraw

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
Or_button = Image.open("OriginalButton.png")
font = ImageFont.truetype('ChalkboardSE-Regular.ttf', 100)

share_static = "If you know anything that you haven't seen in our training program and it might be useful, please add it :)"
share_editable = ImageDraw.Draw(Or_button)
share_editable.text((-25, -80), share_static, (F, F, F), font = font)
Or_button.draw(screen)

back = button.Button(10, 10, back_bttn, 150, 100)

while True:
	screen.blit(background, (0, 0))

	switch_file = 0

	if back.draw(screen):
		switch_file = 1
		break

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

	pygame.display.update()

if switch_file == 1:
	import main

pygame.quit()
