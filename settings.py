import pygame
import button

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)


def settings_func(new_start):
    if back.draw(screen):
        new_start = -1

    for event in pygame.event.get():

        if event.type == pygame.QUIT: exit()

    return new_start
