from screen_info import screen
import pygame
import static
import button
import json

WHITE = (255, 255, 255)

json_data = {
    "question": None,
    "right_answer": None,
	"wrong_answer_1": None,
	"wrong_answer_2": None,
	"wrong_answer_3": None
}

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
	font = pygame.font.SysFont('Comic Sans MS', 40)
	y_offset = 0
	for line in lines:
		fw, fh = font.size(line)

		tx = X - fw / 2
		ty = Y + y_offset

		font_surface = font.render(line, True, WHITE)
		screen.blit(font_surface, (tx, ty))

		y_offset += fh


back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()
correct = pygame.image.load('imgs_updated/Back.png').convert_alpha()
wrong = pygame.image.load('imgs_updated/Back.png').convert_alpha()

bttn = pygame.image.load('imgs_updated/OriginalButton.png').convert_alpha()

back = button.Button(10, 690, back_bttn, 150, 100)
answer_1_button = button.Button(250, 300, bttn, 500, 200)
answer_2_button = button.Button(250, 500, bttn, 500, 200)
answer_3_button = button.Button(790, 300, bttn, 500, 200)
answer_4_button = button.Button(790, 500, bttn, 500, 200)
question_static = static.Static(235, 10, bttn, 1065, 250)
correct_static = static.Static(500, 600, bttn, 1065, 250)
wrong_static = static.Static(235, 10, bttn, 1065, 250)

def single_player_func(new_start):
	with open(".json/questions.json") as jsonFile:
		jsonObject = json.load(jsonFile)
		jsonFile.close()

	question = jsonObject[0]['question']
	right_answer = jsonObject[0]['right_answer']
	wrong_answer_1 = jsonObject[0]['wrong_answer_1']
	wrong_answer_2 = jsonObject[0]['wrong_answer_2']
	wrong_answer_3 = jsonObject[0]['wrong_answer_3']

	question_static.draw(screen)

	is_select = 0
	while is_select == 0:
		if answer_1_button.draw(screen):
			select_button = right_answer
			is_select = 1
			print("Correct")

		if answer_2_button.draw(screen):
			select_button = wrong_answer_2
			is_select = 1
			print("Wrong")

		if answer_3_button.draw(screen):
			select_button = wrong_answer_1
			is_select = 1
			print("Wrong")

		if answer_4_button.draw(screen):
			select_button = wrong_answer_3
			is_select = 1
			print("Wrong")

		if is_select == 1:
			break

		draw(question, 800, 60)
		draw(right_answer, 340, 370)
		draw(wrong_answer_1, 900, 370)
		draw(wrong_answer_2, 340, 570)
		draw(wrong_answer_3, 900, 570)



	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

	pygame.display.update()

	return new_start