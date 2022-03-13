from screen_info import screen
from text import draw
from textwrap import fill
import pygame
import static
import button


background = pygame.image.load("imgs/background.png")
back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
cum = pygame.image.load('imgs_updated/ComingSoon.png').convert_alpha()

cum = static.Static(400, -60, cum, 700, 900)
back = button.Button(10, 690, bttn, 150, 100)

def multi_player_func(new_start):
    screen.blit(background, (0, 0))

    if back.draw(screen):
        new_start = 3
    cum.draw(screen)
    draw("Back", 30, 710, 36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    return new_start

    pygame.display.update()