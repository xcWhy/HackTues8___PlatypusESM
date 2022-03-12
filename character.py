import button
import pygame
import static

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

transparent = 0, 0, 0, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_img = pygame.image.load('imgs/button_assets.png').convert_alpha()
back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
choose_img = pygame.image.load('imgs/ChooseYourAstronaut.png').convert_alpha()
yuri_img = pygame.image.load('imgs/Yuri.png').convert_alpha()
nelson_img = pygame.image.load('imgs/Nelson.png').convert_alpha()
buzz_img = pygame.image.load('imgs/Buzz.png').convert_alpha()
switch_img = pygame.image.load('imgs/ButtonArrow.png').convert_alpha()
astronautw_img = pygame.image.load('imgs_updated/AstronautWhite.png').convert_alpha()
astronautb_img = pygame.image.load('imgs_updated/AstronautBlue.png').convert_alpha()
astronautg_img = pygame.image.load('imgs_updated/AstronautGreen.png').convert_alpha()
astronautr_img = pygame.image.load('imgs_updated/AstronautRed.png').convert_alpha()
spacesuit_img = pygame.image.load('imgs/ChooseYourSpacesuit.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)
choose = static.Static(-25, -80, choose_img, 600, 600)
astr1 = button.Button(4, 80, nelson_img, 500, 500)
astr2 = button.Button(4, 170, yuri_img, 500, 500)
astr3 = button.Button(4, 260, buzz_img, 500, 500)
switch = button.Button(680, 450, switch_img, 1000, 1000)
astronautw = static.Static(400, -170, astronautw_img, 1000, 1000)
astronautb = static.Static(400, -170, astronautb_img, 1000, 1000)
astronautg = static.Static(400, -170, astronautg_img, 1000, 1000)
astronautr = static.Static(400, -170, astronautr_img, 1000, 1000)
spacesuit = static.Static(400, 400, spacesuit_img, 400, 400)

choose.draw(screen)
astronautw.draw(screen)
spacesuit.draw(screen)

background = pygame.image.load("imgs/background.png")

#astronauts_colors = [astronautw, astronautb, astronautg, astronautr]
rechnik = {
            0:astronautw,
            1:astronautb,
            2:astronautg,
            3:astronautr
        }
k = 0
transparent = (0, 0, 0, 0)

personal_astronaut = astronautw

while True:
    screen.blit(background, (0, 0))

    choose.draw(screen)
    personal_astronaut.draw(screen)

    switch_file = 0

    if back.draw(screen):
        switch_file = 1
        break

    if astr1.draw(screen):
        print('Nelson Armstrong')
    
    if astr2.draw(screen):
        print('Yuri Gagarin')
    
    if astr3.draw(screen):
        print('Buzz Aldrin')

    if switch.draw(screen):
        
        #rechnik[k].draw(screen)
        personal_astronaut = rechnik[k]
        k += 1
        #print(personal_astronaut)
        if k == 4:
            k = 0
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

if switch_file == 1:
    import main

pygame.quit()

