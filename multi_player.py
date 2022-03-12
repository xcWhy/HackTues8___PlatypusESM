from textwrap import fill
import pygame
import static
import button
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1535

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("imgs/background.png")

back_bttn = pygame.image.load('imgs_updated/Back.png').convert_alpha()

back = button.Button(10, 10, back_bttn, 150, 100)

org_bttn = Image.open("imgs_updated/OriginalButton.png")
choose_category = ImageDraw.Draw(org_bttn)

Font = ImageFont.truetype('ChalkboardSE-Regular.ttf',125)
choose_category.text((130,70),"Choose your category", font=Font, fill=(255,255,255))
org_bttn.save('imgs_updated/ChooseYourCategory.png')

choose_ctgr = pygame.image.load('imgs_updated/ChooseYourCategory.png').convert_alpha()
cat_bttn = button.Button(575,100,choose_ctgr,400,100)


org_bttn1 = Image.open("imgs_updated/OriginalButton.png")
engineer = ImageDraw.Draw(org_bttn1)

Font = ImageFont.truetype('ChalkboardSE-Regular.ttf',125)
engineer.text((450,70),"Engineer", font=Font, fill=(255,255,255))
org_bttn1.save("imgs_updated/Engineer.png")

eng = pygame.image.load('imgs_updated/Engineer.png').convert_alpha()
eng_bttn = button.Button(575,250,eng,400,100)


org_bttn1 = Image.open("imgs_updated/OriginalButton.png")
mathematician = ImageDraw.Draw(org_bttn1)

Font = ImageFont.truetype('ChalkboardSE-Regular.ttf',125)
mathematician.text((300,70),"Mathematician", font=Font, fill=(255,255,255))
org_bttn1.save("imgs_updated/Mathematician.png")

math = pygame.image.load('imgs_updated/Mathematician.png').convert_alpha()
math_bttn = button.Button(575,400,math,400,100)


org_bttn1 = Image.open("imgs_updated/OriginalButton.png")
medician = ImageDraw.Draw(org_bttn1)

Font = ImageFont.truetype('ChalkboardSE-Regular.ttf',125)
medician.text((450,70),"Medicine", font=Font, fill=(255,255,255))
org_bttn1.save("imgs_updated/Medicine.png")

medic = pygame.image.load('imgs_updated/Medicine.png').convert_alpha()
medic_bttn = button.Button(575,550,medic,400,100)


org_bttn1 = Image.open("imgs_updated/OriginalButton.png")
bio = ImageDraw.Draw(org_bttn1)

Font = ImageFont.truetype('ChalkboardSE-Regular.ttf',125)
bio.text((500,70),"Biology", font=Font, fill=(255,255,255))
org_bttn1.save("imgs_updated/Biology.png")

biology = pygame.image.load('imgs_updated/Biology.png').convert_alpha()
biology_bttn = button.Button(575,700,biology,400,100)


run = True
while run:
	screen.blit(background, (0, 0))


	if back.draw(screen):
		switch_file = 1
		break

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

if switch_file == 1:
	import quiz

pygame.quit()
