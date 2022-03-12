import button
import pygame
import static

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
choose_img = pygame.image.load('imgs_updated/ChooseYourAstronaut.png').convert_alpha()
yuri_img = pygame.image.load('imgs_updated/Yuri.png').convert_alpha()
yuri_reverse_img = pygame.image.load('imgs_updated/Yuri2.png').convert_alpha()
nelson_img = pygame.image.load('imgs_updated/Nelson.png').convert_alpha()
nelson_reverse_img = pygame.image.load('imgs_updated/Nelson2.png').convert_alpha()
buzz_img = pygame.image.load('imgs_updated/Buzz.png').convert_alpha()
buzz_reverse_img = pygame.image.load('imgs_updated/Buzz2.png').convert_alpha()
reverse_img = pygame.image.load('imgs_updated/UnoReverse.png').convert_alpha()
astronautw_img = pygame.image.load('imgs_updated/AstronautWhite.png').convert_alpha()
astronautb_img = pygame.image.load('imgs_updated/AstronautBlue.png').convert_alpha()
astronautg_img = pygame.image.load('imgs_updated/AstronautGreen.png').convert_alpha()
astronautr_img = pygame.image.load('imgs_updated/AstronautRed.png').convert_alpha()
spacesuit_img = pygame.image.load('imgs_updated/ChooseYourSpacesuit.png').convert_alpha()


back = button.Button(10, 10, back_bttn, 150, 100)
choose = static.Static(130, 165, choose_img, 350, 75)
Nelson = button.Button(130, 270, nelson_img, 350, 75)
Yuri = button.Button(130, 355, yuri_img, 350, 75)
Buzz = button.Button(130, 440, buzz_img, 350, 75)
Nelson_reverse = button.Button(130, 270, nelson_reverse_img, 650, 375)
Yuri_reverse = button.Button(130, 355, yuri_reverse_img, 350, 75)
Buzz_reverse = button.Button(130, 440, buzz_reverse_img, 350, 75)
reverse = button.Button(1140, 675, reverse_img, 75, 75)
astronautw = static.Static(400, -170, astronautw_img, 1000, 1000)
astronautb = static.Static(400, -170, astronautb_img, 1000, 1000)
astronautg = static.Static(400, -170, astronautg_img, 1000, 1000)
astronautr = static.Static(400, -170, astronautr_img, 1000, 1000)
spacesuit = static.Static(1000, 600, spacesuit_img, 350, 75)

def character_func(new_start):
    choose.draw(screen)
    astronautw.draw(screen)
    spacesuit.draw(screen)

    astronaut_1 = False
    astronaut_2 = False
    astronaut_3 = False

    list = {
        0: astronautr,
        1: astronautg,
        2: astronautb,
        3: astronautw
    }

    personal_astronaut = astronautw
    k = 0

    while new_start == 1:
        choose.draw(screen)
        personal_astronaut.draw(screen)

        if back.draw(screen):
            new_start = 0

        if Nelson.draw(screen):
            print("Nelson")

        if Yuri.draw(screen):
            print("Yuri")

        if Buzz.draw(screen):
            print("Buzz")

        if astronaut_1 == True:
            Nelson_reverse.draw(screen)

        if reverse.draw(screen):
            personal_astronaut = list[k]
            k += 1
            if k == 4:
                k = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()

    return new_start

