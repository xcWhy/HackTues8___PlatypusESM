import pygame
import button
import static
from screen_info import screen
from text import draw

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("imgs/background.png")

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
board = pygame.image.load('imgs_updated/TipBoard.png').convert_alpha()

Credit = static.Static(960, 10, bttn, 400, 100)
Imena = static.Static(870, -20, board, 700, 700)
back = button.Button(10, 10, bttn, 155, 100)
resolution = button.Button(10, 680, bttn, 250, 100)



def settings_func(new_start):
    if back.draw(screen):
        new_start = -1
    if resolution.draw(screen):
        print("resolution")

    Credit.draw(screen)
    Imena.draw(screen)

    draw("Credits to:", 1020, 30, 36)
    draw("Back", 40, 30, 36)
    draw("Елена Чернева 9г", 1000, 150, 32)
    draw("Стефани Пенчева 9г", 1000, 190, 32)
    draw("Емилиана Петренко 10б", 1000, 230, 32)
    draw("Магдалена Никифорова 9г", 1000, 270, 32)
    draw("Нейчо Калайджиев - ментор", 1000, 310, 32)
    draw("проект - Spacequiz", 1000, 350, 32)
    draw("HackTues 8 - 2022", 1000, 390, 32)
    draw("resolution", 50, 700, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    return new_start
