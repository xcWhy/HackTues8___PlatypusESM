from screen_info import screen
from text import draw
import button
import pygame
import static
import json

############################ JSON DATA ############################

json_data = {
    "astronaut": None,
    "color": None
}

###################################################################

######################## Images & Buttons #########################

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
select_bttn = pygame.image.load('imgs_updated/ReverseButton.png').convert_alpha()

back_button = button.Button(10, 10, bttn, 150, 100)
choose_astronaut = static.Static(130, 165, bttn, 350, 75)
Nelson_Armstrong = button.Button(130, 270, bttn, 350, 75)
select_Nelson_Armstrong = button.Button(130, 270, select_bttn, 350, 75)
Yuri_Gagarin = button.Button(130, 355, bttn, 350, 75)
select_Yuri_Gagarin = button.Button(130, 355, select_bttn, 350, 75)
Buzz_Aldrin = button.Button(130, 440, bttn, 350, 75)
select_Buzz_Aldrin = button.Button(130, 440, select_bttn, 350, 75)
spacesuit = static.Static(1000, 600, bttn, 350, 75)

astronaut_white= pygame.image.load('imgs_updated/AstronautWhite.png').convert_alpha()
astronaut_white_static = static.Static(400, -170, astronaut_white, 1000, 1000)

astronaut_blue = pygame.image.load('imgs_updated/AstronautBlue.png').convert_alpha()
astronaut_blue_static = static.Static(400, -170, astronaut_blue, 1000, 1000)

astronaut_green = pygame.image.load('imgs_updated/AstronautGreen.png').convert_alpha()
astronaut_green_static = static.Static(400, -170, astronaut_green, 1000, 1000)

astronaut_red = pygame.image.load('imgs_updated/AstronautRed.png').convert_alpha()
astronaut_red_static = static.Static(400, -170, astronaut_red, 1000, 1000)

swap = pygame.image.load('imgs_updated/UnoReverse.png').convert_alpha()
swap_button = button.Button(1140, 675, swap, 75, 75)

#####################################################################

def character_func(new_start):
    with open(".json/character.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    astronaut = jsonObject['astronaut']
    color = jsonObject['color']


    choose_astronaut.draw(screen)
    astronaut_white_static.draw(screen)
    spacesuit.draw(screen)

    list = {
        0: astronaut_red_static,
        1: astronaut_green_static,
        2: astronaut_blue_static,
        3: astronaut_white_static
    }

    if color == 0:
        personal_astronaut = list[3]
    else:
        personal_astronaut = list[color-1]
    k = color

    while new_start == 1:
        choose_astronaut.draw(screen)
        personal_astronaut.draw(screen)

        if back_button.draw(screen):
            new_start = 0


        if astronaut == 'Nelson Armstrong':
            if select_Nelson_Armstrong.draw(screen):
                astronaut = "Nelson Armstrong"

            if Yuri_Gagarin.draw(screen):
                astronaut = "Yuri Gagarin"

            if Buzz_Aldrin.draw(screen):
                astronaut = "Buzz Aldrin"

        if astronaut == 'Yuri Gagarin':
            if Nelson_Armstrong.draw(screen):
                astronaut = "Nelson Armstrong"

            if select_Yuri_Gagarin.draw(screen):
                astronaut = "Yuri Gagarin"

            if Buzz_Aldrin.draw(screen):
                astronaut = "Buzz Aldrin"

        if astronaut == 'Buzz Aldrin':
            if Nelson_Armstrong.draw(screen):
                astronaut = "Nelson Armstrong"

            if Yuri_Gagarin.draw(screen):
                astronaut = "Yuri Gagarin"

            if select_Buzz_Aldrin.draw(screen):
                astronaut = "Buzz Aldrin"


        if swap_button.draw(screen):
            personal_astronaut = list[k]
            k += 1
            if k == 4:
                k = 0

            color = k

        draw("Back", 45, 35, 36)
        draw("Choose your astronaut", 150, 180, 30)
        draw("Nelson Armstrong", 180, 285, 30)
        draw("Yuri Gagarin", 220, 370, 30)
        draw("Buzz Aldrin", 225, 455, 30)
        draw("Choose your spacesuit", 1025, 615, 30)


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



