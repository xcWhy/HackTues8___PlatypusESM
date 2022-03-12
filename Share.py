import pygame
import pygame_textinput
import static
import button

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
share_bttn = pygame.image.load('imgs_updated/IfYouHavnetSeen.png').convert_alpha()
type_space = pygame.image.load('imgs_updated/TipBoard.png').convert_alpha()
send = pygame.image.load('imgs_updated/Send.png').convert_alpha()

send_button = button.Button(700, 675, send, 150, 100)
back = button.Button(10, 10, back_bttn, 150, 100)
share = static.Static(375, 50, share_bttn, 800, 200)
type = static.Static(260, 140, type_space, 1000 ,800)

textinput = pygame_textinput.TextInputVisualizer()

font = pygame.font.SysFont(r'C:\Users\MAGI\Desktop\HackTues8___PlatypusESM\font\ChalkboardSE-Regular.ttf', 32)

def blit_text(share_bttn, textinput, pos, font, color=pygame.Color('white')):
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
    share.draw(screen)
    type.draw(screen)

    events = pygame.event.get()

    textinput.update(events)
    screen.blit(textinput.surface, (460, 375))

    if send_button.draw(screen):
        print("Send")

    if back.draw(screen):
    	new_start = 0

    for event in pygame.event.get():
    	if event.type == pygame.QUIT: exit()

    pygame.display.update()

    return new_start

