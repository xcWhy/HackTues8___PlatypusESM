from text import draw
import pygame
import pygame_textinput
import static
import button

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()
type_space = pygame.image.load('imgs_updated/TipBoard.png').convert_alpha()

send_button = button.Button(700, 675, bttn, 150, 100)
back_button = button.Button(10, 10, bttn, 150, 100)
share_knowledge = static.Static(375, 50, bttn, 800, 200)
type_static = static.Static(260, 140, type_space, 1000 ,800)

textinput = pygame_textinput.TextInputVisualizer()

font = pygame.font.SysFont(r'C:\Users\MAGI\Desktop\HackTues8___PlatypusESM\font\ChalkboardSE-Regular.ttf', 32)

def blit_text(share_knowledge, textinput, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def share_func(new_start):
    share_knowledge.draw(screen)
    type_static.draw(screen)

    events = pygame.event.get()

    textinput.update(events)
    screen.blit(textinput.surface, (460, 375))

    if back_button.draw(screen):
    	new_start = 0

    if send_button.draw(screen):
    	print("Send")

    for event in pygame.event.get():
    	if event.type == pygame.QUIT: exit()

    draw("Send", 735, 700, 32)
    draw("Back", 50, 35, 32)
    draw("if you know anything, that you haven't seen in our training program, please add it", 450, 135, 18)

    pygame.display.update()

    return new_start

