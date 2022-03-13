from screen_info import screen
from text import draw
import pygame
import button
import static

background = pygame.image.load("imgs_updated/Start_Screen.png").convert_alpha()
background_static = static.Static(0, -100, background, 1535, 900)

settings = pygame.image.load('imgs_updated/Settings.png').convert_alpha()
bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

settings_button = button.Button(10, 10, settings, 150, 100)
menu_button = button.Button(1240, 5, bttn, 150, 100)
exit_button = button.Button(1390, 5, bttn, 130, 100)

def homepage_func(new_start):
    background_static.draw(screen)

    if settings_button.draw(screen):
        new_start = -2

    if menu_button.draw(screen):
        new_start = 0

    if exit_button.draw(screen):
        exit()

    draw("Menu", 1275, 30, 36)
    draw("Exit", 1425, 30, 36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

    return new_start