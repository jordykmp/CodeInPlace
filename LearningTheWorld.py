import random
import pygame
import time
from pygame import mixer

'''Initializing Pygame'''

pygame.init()

#creating the screen
size = 800, 600
screen = pygame.display.set_mode(size)

#Background
#background = pygame.image.load('image name here') '''descargar imagen de fondo'''

#Background sound
#mixer.music.load('musica name here') '''Descargar audio de fondo'''
#mixer.music.play(-1) '''playing on loop'''


#Title and Icon
pygame.display.set_caption('LEARNING THE WORLD') #32x32 in draw.io
icon = pygame.image.load('earth.png')
pygame.display.set_icon(icon)

#Looping Game
running = True

while running:
    for event in pygame.event.get():
        #Closing window
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255,0,0)) #RGB values
    pygame.display.update()
    #show_text(textX,textY)
    ''' here comes sound of correct answer chosen'''
    #correct_sound = mixer.sound('Sound name here')
    #correct_sound.play()
    
#adding text
#font = 'ASIA'
#font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Function that allows adding text to show it on the screen
def show_text(x,y):
    text = font.render('Your continent for learn is: '+texto, True, (255,255,255))
    screen.blit(text, (x,y))
