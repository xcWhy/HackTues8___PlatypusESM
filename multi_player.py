from textwrap import fill
import pygame
import static
import button

switch_file=0

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)


choose_ctgr = pygame.image.load('imgs_updated/ChooseYourCategory.png').convert_alpha()
category = button.Button(575, 50, choose_ctgr, 400, 100)


eng = pygame.image.load('imgs_updated/Engineer.png').convert_alpha()
engineer = button.Button(575, 200, eng, 400, 100)


math = pygame.image.load('imgs_updated/Mathematician.png').convert_alpha()
mathematics = button.Button(575, 350, math, 400, 100)


medic = pygame.image.load('imgs_updated/Medicine.png').convert_alpha()
medicine = button.Button(575, 500, medic, 400, 100)


biology = pygame.image.load('imgs_updated/Biology.png').convert_alpha()
bio = button.Button(575, 650, biology, 400, 100)



run = True
while run:
    screen.blit(background, (0, 0))
    if category.draw(screen):
        print("1")
    elif engineer.draw(screen):
        print("2")
    elif mathematics.draw(screen):
        print("3")
    elif medicine.draw(screen):
        print("4")
    elif bio.draw(screen):
        print("5")
    elif back.draw(screen):
        switch_file = 1
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

if switch_file == 1:
	import quiz

pygame.quit()
