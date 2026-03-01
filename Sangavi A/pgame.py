import pygame, sys

""" pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit() """


""" pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         key=pygame.key.name(event.key)
         print (key, "Key is pressed")
      if event.type == pygame.KEYUP:
         key=pygame.key.name(event.key)
         print (key, "Key is released") """

""" pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
   pygame.draw.rect(screen, red, pygame.Rect(100, 30, 60, 60))
   pygame.draw.polygon(screen, blue, ((25,75),(76,125),(275,200),(350,25),(60,280)))
   pygame.draw.circle(screen, white, (180,180), 60)
   pygame.draw.line(screen, red, (10,200), (300,10), 4)
   pygame.draw.ellipse(screen, green, (250, 200, 130, 80)) 
   pygame.display.update() """

""" import pygame
from pygame.locals import *
from sys import exit

image_filename = 'Dodge-Challenger.png'

pygame.init()
screen = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Moving Image")
img = pygame.image.load(image_filename)
x = 0
while True:
   screen.fill((255,255,255))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
   screen.blit(img, (x, 100))
   x= x+0.5

   if x > 400:
      x = x-400
   pygame.display.update() """

""" import pygame
from pygame.locals import *
from sys import exit

image_filename = 'Dodge-Challenger.png'

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Moving with arrows")
img = pygame.image.load(image_filename)
x = 0
y= 0
while True:
   screen.fill((255,255,255))
   screen.blit(img, (x, y))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()

      if event.type == KEYDOWN:
         if event.key == K_RIGHT:
            x= x+5
         if event.key == K_LEFT:
            x=x-5
         if event.key == K_UP:
            y=y-5
         if event.key == K_DOWN:
            y=y+5
         pygame.display.update() """


""" import pygame
from pygame.locals import *
from sys import exit

pygame.init()

filename = 'Dodge-Challenger.png'

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Moving with mouse")
img = pygame.image.load(filename)
x = 0
y= 0
while True:
   mx,my=pygame.mouse.get_pos()
   screen.fill((255,255,255))
   screen.blit(img, (mx, my))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      pygame.display.update() """


""" import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

font = pygame.font.SysFont("Arial", 14)
text1=font.render(" START ", True, 'white')
text2=font.render(" PLAY ", True, 'white')
text3=font.render(" STOP ", True, 'white')

rect1 = text1.get_rect(topleft=(10,10))
rect2 = text2.get_rect(topleft= (100,10))
rect3 = text3.get_rect(topleft= (200,10))
bg = (127,127,127)
msg=" "
screen = pygame.display.set_mode((400,300))
screen.fill(bg)
while not done:
   for event in pygame.event.get():
      screen.blit(text1, rect1)
      pygame.draw.rect(screen, (255,0,0),rect1,2)
      screen.blit(text2, rect2)
      pygame.draw.rect(screen, (255,0,0),rect2,2)
      pygame.draw.rect(screen, (255,0,0),rect3,2)
      screen.blit(text3, rect3)
      
      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         if rect1.collidepoint(event.pos):
            msg = "START Button was pressed"
         if rect2.collidepoint(event.pos):
            msg = "PLAY Button was pressed"
         if rect3.collidepoint(event.pos):
            msg = "STOP Button was pressed"
      img=font.render(msg, True, (0,0,255))
      imgrect=img.get_rect()
      imgrect.center = (200 , 150 )
      pygame.draw.rect(screen, bg, imgrect)
      screen.blit(img, imgrect)

   pygame.display.update() """


""" import pygame 
pygame.init() 

win = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Moving rectangle") 

x = 200
y = 200

width = 20
height = 20

vel = 10
run = True

# infinite loop 
while run: 
	pygame.time.delay(10) 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False
	keys = pygame.key.get_pressed() 
	
	if keys[pygame.K_LEFT] and x>0: 
		x -= vel 
		
	if keys[pygame.K_RIGHT] and x<500-width: 
		x += vel 
		
	if keys[pygame.K_UP] and y>0: 
		y -= vel 
		
	if keys[pygame.K_DOWN] and y<500-height: 
		y += vel 
		
	win.fill((0, 0, 0)) 
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
	pygame.display.update() 

pygame.quit() """