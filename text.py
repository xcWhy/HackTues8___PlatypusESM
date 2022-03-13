from screen_info import screen
import pygame

def draw(text, X, Y, Size):
	pygame.init()
	font = pygame.font.SysFont('Comic Sans MS', Size)
	paragraph = font.render(text, True, (255,255,255))
	screen.blit(paragraph, (X, Y))
