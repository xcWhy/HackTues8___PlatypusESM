import pygame
import static
import button
import json

json_data = {
	"question": None,
	"answer": None
}

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

def draw(text, X, Y):

	pygame.init()
	letters = []
	lettersCount = len(text)

	for i in range(0, lettersCount):
		letters.append(text[i])
		if i % 30 == 0 and i != 0:
			letters.append("\n\r")
	text = "".join(letters)

	lines = text.split("\n\r")
	font = pygame.font.SysFont('Comic Sans MS', 24)
	y_offset = 0
	for line in lines:
		fw, fh = font.size(line)

		tx = X - fw / 2
		ty = Y + y_offset

		font_surface = font.render(line, True, WHITE)
		screen.blit(font_surface, (tx, ty))

		y_offset += fh

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
question = pygame.image.load('imgs_updated/FlashCard_Template.png').convert_alpha()
answer = pygame.image.load('imgs_updated/FlashCard_Template.png').convert_alpha()
reverse = pygame.image.load('imgs_updated/UnoReverse.png').convert_alpha()
next = pygame.image.load('imgs_updated/Next.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)
question_static = static.Static(450, 100, question, 650, 600)
answer_static = static.Static(450, 100, answer, 650, 600)
reverse_button = button.Button(615, 550, reverse, 100, 100)
next_button = button.Button(750, 550, next, 150, 100)

def training_func(new_start):
	with open(".json/training.json", encoding="utf8") as jsonFile:
		jsonObject = json.load(jsonFile)
		jsonFile.close()

	i = 0

	question = jsonObject[i]['question']
	answer = jsonObject[i]['answer']


	flip = True

	question_static.draw(screen)
	draw(question, 750, 350)
	while new_start == 2:

		if reverse_button.draw(screen):
			if flip == False:
				flip = True
			else:
				flip = False

			if flip:
				answer_static.draw(screen)
				draw(answer, 750, 350)
			else:
				question_static.draw(screen)
				draw(question, 750, 350)

		if back.draw(screen):
			new_start = 0

		if next_button.draw(screen):
			if question != "END":
				draw(question, 750, 350)
			else:
				i = 0

			i += 1

			question = jsonObject[i]['question']
			answer = jsonObject[i]['answer']


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		pygame.display.update()

	return new_start
