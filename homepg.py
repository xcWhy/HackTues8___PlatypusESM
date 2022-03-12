import pygame
import button
import static

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("imgs_updated/Start_Screen.png").convert_alpha()
set_bttn = pygame.image.load('imgs_updated/Settings.png').convert_alpha()
menu = pygame.image.load('imgs_updated/Menu.png').convert_alpha()
exit = pygame.image.load('imgs_updated/Exit.png').convert_alpha()

bckg = static.Static(0, -100, background, 1535, 900)
exit_button = button.Button(1390, 5, exit, 130, 100)
set = button.Button(10, 10, set_bttn, 150, 100)
menu_button = button.Button(1240, 5, menu, 150, 100)

def homepage_func(new_start):
    bckg.draw(screen)

    if set.draw(screen):
        print("Set")

    if menu_button.draw(screen):
        new_start = 0

    if exit_button.draw(screen):
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

    return new_start