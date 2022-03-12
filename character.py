import button
import pygame
import static
import json

############################ JSON DATA ############################
json_data = {
    "astronaut": None,
    "color": None
}

############################### SCREEN #############################
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


############################## BUTTONS #############################
back = pygame.image.load('imgs_updated/Back.png').convert_alpha()
back_button = button.Button(10, 10, back, 150, 100)

reverse_img = pygame.image.load('imgs_updated/UnoReverse.png').convert_alpha()
reverse = button.Button(1140, 675, reverse_img, 75, 75)


############################ ASTRONAUTS ############################
choose_img = pygame.image.load('imgs_updated/ChooseYourAstronaut.png').convert_alpha()
choose = static.Static(130, 165, choose_img, 350, 75)

nelson_img = pygame.image.load('imgs_updated/Nelson.png').convert_alpha()
Nelson = button.Button(130, 270, nelson_img, 350, 75)

nelson_reverse_img = pygame.image.load('imgs_updated/Nelson2.png').convert_alpha()
Nelson_reverse = button.Button(130, 270, nelson_reverse_img, 350, 75)

yuri_img = pygame.image.load('imgs_updated/Yuri.png').convert_alpha()
Yuri = button.Button(130, 355, yuri_img, 350, 75)

yuri_reverse_img = pygame.image.load('imgs_updated/Yuri2.png').convert_alpha()
Yuri_reverse = button.Button(130, 355, yuri_reverse_img, 350, 75)

buzz_img = pygame.image.load('imgs_updated/Buzz.png').convert_alpha()
Buzz = button.Button(130, 440, buzz_img, 350, 75)

buzz_reverse_img = pygame.image.load('imgs_updated/Buzz2.png').convert_alpha()
Buzz_reverse = button.Button(
     130, 440, buzz_reverse_img, 350, 75)


########################## CHARACTER ################################
spacesuit_img = pygame.image.load('imgs_updated/ChooseYourSpacesuit.png').convert_alpha()
spacesuit = static.Static(1000, 600, spacesuit_img, 350, 75)

astronautw_img = pygame.image.load('imgs_updated/AstronautWhite.png').convert_alpha()
astronautw = static.Static(400, -170, astronautw_img, 1000, 1000)

astronautb_img = pygame.image.load('imgs_updated/AstronautBlue.png').convert_alpha()
astronautb = static.Static(400, -170, astronautb_img, 1000, 1000)

astronautg_img = pygame.image.load('imgs_updated/AstronautGreen.png').convert_alpha()
astronautg = static.Static(400, -170, astronautg_img, 1000, 1000)

astronautr_img = pygame.image.load('imgs_updated/AstronautRed.png').convert_alpha()
astronautr = static.Static(400, -170, astronautr_img, 1000, 1000)


def character_func(new_start):
    with open(".json/character.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    astronaut = jsonObject['astronaut']
    color = jsonObject['color']

    print(astronaut, color)

    with open('writed_json.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close()

    choose.draw(screen)
    astronautw.draw(screen)
    spacesuit.draw(screen)

    list = {
        0: astronautr,
        1: astronautg,
        2: astronautb,
        3: astronautw
    }

    if color == 0:
        personal_astronaut = list[3]
    else:
        personal_astronaut = list[color-1]
    k = color

    while new_start == 1:
        choose.draw(screen)
        personal_astronaut.draw(screen)

        if back_button.draw(screen):
            new_start = 0


        if astronaut == 'Nelson Armstrong':
            if Nelson_reverse.draw(screen):
                astronaut = "Nelson Armstrong"

            if Yuri.draw(screen):
                astronaut = "Yuri Gagarin"

            if Buzz.draw(screen):
                astronaut = "Buzz Aldrin"

        if astronaut == 'Yuri Gagarin':
            if Nelson.draw(screen):
                astronaut = "Nelson Armstrong"

            if Yuri_reverse.draw(screen):
                astronaut = "Yuri Gagarin"

            if Buzz.draw(screen):
                astronaut = "Buzz Aldrin"

        if astronaut == 'Buzz Aldrin':
            if Nelson.draw(screen):
                astronaut = "Nelson Armstrong"

            if Yuri.draw(screen):
                astronaut = "Yuri Gagarin"

            if Buzz_reverse.draw(screen):
                astronaut = "Buzz Aldrin"


        if reverse.draw(screen):
            personal_astronaut = list[k]
            k += 1
            if k == 4:
                k = 0

            color = k

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()

    json_data["astronaut"] = astronaut
    json_data["color"] = color

    with open('.json/character.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close()
        print("Done")



    return new_start



