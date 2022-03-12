import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


background = pygame.image.load("imgs/background.png")

set_bttn = pygame.image.load('imgs_updated/Settings.png').convert_alpha()

set = button.Button(10, 10, set_bttn, 150, 100)



while True:
    screen.blit(background, (0, 0))

    switch_file = 0

    if back.draw(screen):
        switch_file = 1
        break

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

if switch_file == 1:
	import settings

pygame.quit()