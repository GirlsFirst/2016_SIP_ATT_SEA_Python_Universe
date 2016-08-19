#first level
#objective is to get the character to the end of the maze with functions

"""
 Python Universe
 Jisook & Malia
"""
#import stuff

import pygame, string
import random
import time
import sys
from pygame.locals import*
import eztext
from StarClass import Stars

oxyScore = 0

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

##play music
pygame.mixer.music.load("8-bit-Arcade4.mp3")
pygame.mixer.music.play(70)

# Set the width and height of the screen [width, height]
size_width = (1366)
size_height = (768)
gameDisplay = pygame.display.set_mode((size_width,size_height))

##display oxygen
oxy1 = pygame.image.load('oxygen.png')
oxy2 = pygame.image.load('oxygen.png')
oxy3 = pygame.image.load('oxygen.png')

##scaled oxygen
scaledOxy1 = pygame.transform.scale(oxy1,[112,112])
scaledOxy2 = pygame.transform.scale(oxy2,[112,112])
scaledOxy3 = pygame.transform.scale(oxy3,[112,112])


##display character
characterGirl = pygame.image.load('malia.gif')

##display background image
background = pygame.image.load('firstLevelBackground.png')

textbox = eztext.Input(maxlength = 70, color = (WHITE), prompt = '')


##class Character():
##
##    def __init__(self, x_speed, y_speed, x_position, y_position):
##        self.x_speed = x_speed
##        self.y_speed = y_speed
##        self.x_position = x_position
##        self.y_position = y_position
##
##    def x_move(self, x_speed):
##        self.x_location += x_speed
##
##    def y_move(self, y_speed):
##        self.y_location -= y_speed

##character = Character(288,288,291,241)

pygame.display.set_caption("Python Universe")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Star List
star_list = []

x_move = 291
y_move = 241

oxy_loc = [530,220]
oxy_loc2 = [540,496]
oxy_loc3 = [808,506]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            
    gameDisplay.fill(BLACK)

    ##display te
##    xtbox       
    textbox.update(events)
    textbox.draw(gameDisplay)
    print(textbox.anyThing)

    if textbox.anyThing == 'moveRight()':
        x_move = 569
        y_move = 241
        oxy_loc = [1000,1000]
        oxyScore+=1
        
    if textbox.anyThing == 'moveDown()':
        x_move = 579
        y_move = 517
        oxy_loc2 = [1000,1000]
        oxyScore+=1
        
    if textbox.anyThing == 'moveRightAgain()':
        x_move = 847
        y_move = 527
        oxy_loc3 = [1000,1000]
        oxyScore+=1
    
    
    ##random variables
    randomX = random.randint (0,1350)
    randomY = random.randint (0,750)
    randomSize = random.randint (1,2)
    speed = random.randint (1,2)

    mouse = pygame.mouse.get_pos()
##    print(mouse)
    
    star_list.append(Stars(gameDisplay,WHITE, [randomX, randomY], speed, randomSize)) 
    for i in star_list:
        i.draw()
        i.fall()

    ##display background
    gameDisplay.blit(background,[171,10]) 

    ##display guy
    gameDisplay.blit(characterGirl, [x_move,y_move])
    ##display oxygen
    gameDisplay.blit(scaledOxy1,oxy_loc)
    gameDisplay.blit(scaledOxy2,oxy_loc2)
    gameDisplay.blit(scaledOxy3,oxy_loc3)

    ##score prompt text
    displayScoreFont = pygame.font.Font('mini_pixel-7.ttf',50)
    displayScoreText = displayScoreFont.render('Score:',1,WHITE)
    gameDisplay.blit(displayScoreText, [1114,54])
    
    ##display score
    scoreFont = pygame.font.Font('mini_pixel-7.ttf',50)
    scoreText = scoreFont.render(str(oxyScore),1,(WHITE))
    gameDisplay.blit(scoreText,[1240,54])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()











