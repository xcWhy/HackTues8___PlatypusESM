import pygame
import button
import static

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("imgs_updated/Start_Screen.png").convert_alpha()
set_bttn = pygame.image.load('imgs_updated/Settings.png').convert_alpha()

bckg = static.Static(0, -100, background, 1535, 900)
set = button.Button(10, 10, set_bttn, 150, 100)

while True:
    #screen.blit(background, (0, 0))
    bckg.draw(screen)
    switch_file = 0

    if set.draw(screen):
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