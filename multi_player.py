import pygame
import button
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

switch_file=0

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)

quest1 = pygame.image.load('imgs_updated/Eng_quest1.png').convert_alpha()
quest_bttn = button.Button(575, 50, quest1, 400, 100)

org_bttn = Image.open("imgs_updated/OriginalButton.png")
answer1 = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
answer1.text((550,50),"hull", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Eng_answ1.png")

answ1 = pygame.image.load('imgs_updated/Eng_answ1.png').convert_alpha()
answ1_bttn = button.Button(350, 400, answ1, 400, 100)


org_bttn = Image.open("imgs_updated/OriginalButton.png")
answer2 = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
answer2.text((550,50),"peak", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Eng_answ2.png")

answ2 = pygame.image.load('imgs_updated/Eng_answ2.png').convert_alpha()
answ2_bttn = button.Button(350, 550, answ2, 400, 100)


org_bttn = Image.open("imgs_updated/OriginalButton.png")
answer3 = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
answer3.text((550,50),"snout", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Eng_answ3.png")

answ3 = pygame.image.load('imgs_updated/Eng_answ3.png').convert_alpha()
answ3_bttn = button.Button(800, 400, answ3, 400, 100)


org_bttn = Image.open("imgs_updated/OriginalButton.png")
answer4 = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
answer4.text((550,50),"fairing", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Eng_answ4.png")

answ4 = pygame.image.load('imgs_updated/Eng_answ4.png').convert_alpha()
answ4_bttn = button.Button(800, 550, answ4, 400, 100)


org_bttn = Image.open("imgs_updated/OriginalButton.png")
wrong = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
wrong.text((550,50),"WRONG ANSWER!", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Wrong_answ.png")

wrongg = pygame.image.load('imgs_updated/Wrong_answ.png').convert_alpha()
wrong_bttn = button.Button(770, 400, wrongg, 400, 100)


org_bttn = Image.open("imgs_updated/OriginalButton.png")
right = ImageDraw.Draw(org_bttn)
Font = ImageFont.truetype('imgs_updated/ChalkboardSE-Regular.ttf',125)
right.text((550,50),"RIGHT ANSWER!", font=Font, fill=(255,255,255))
org_bttn.save("imgs_updated/Right_answ.png")

rightt = pygame.image.load('imgs_updated/Right_answ.png').convert_alpha()
right_bttn = button.Button(770, 400, rightt, 400, 100)

run = True
while run:
    screen.blit(background, (0, 0))

    quest_bttn.draw(screen)

    if answ1_bttn.draw(screen):
        wrong_bttn.draw(screen)

    if answ2_bttn.draw(screen):
        right_bttn.draw(screen)
    if answ3_bttn.draw(screen):
        wrong_bttn.draw(screen)
    if answ4_bttn.draw(screen):
        wrong_bttn.draw(screen)
    
    if back.draw(screen):
        switch_file = 1
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

if switch_file == 1:
	import quiz

pygame.quit()
