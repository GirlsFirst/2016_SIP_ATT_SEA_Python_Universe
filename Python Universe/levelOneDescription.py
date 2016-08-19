"""
 Python Universe
 Jisook & Malia
"""
#import stuff
import pygame
import random
import time
import sys
from pygame.locals import*
import eztext
from StarClass import Stars

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

##display some text
promptFont = pygame.font.Font('mini_pixel-7.ttf',80)
functionFont = pygame.font.Font('mini_pixel-7.ttf',60)

continueFont = pygame.font.Font('mini_pixel-7.ttf',50)

# Set the width and height of the screen [width, height]
size_width = (1366)
size_height = (768)
gameDisplay = pygame.display.set_mode((size_width,size_height))

pygame.display.set_caption("Python Universe")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Star List
star_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                import levelOne


    gameDisplay.fill(BLACK)
    
    ##random variables
    randomX = random.randint (0,1350)
    randomY = random.randint (0,750)
    randomSize = random.randint (1,2)
    speed = random.randint (1,2)
    
    star_list.append(Stars(gameDisplay, WHITE, [randomX, randomY], speed, randomSize)) 
    for i in star_list:
        i.draw()
        i.fall()

    ##display level description text
    promptText = promptFont.render('Move your character using functions to obtain all of',1,WHITE)
    promptText2 = promptFont.render('the oxygen on the screen!',1,WHITE)

    ##display function text
    functionTextRight = functionFont.render("the 'moveRight()' function moves your character to the right",1,WHITE)
    functionTextDown = functionFont.render("the 'moveDown()' function moves your character down",1,WHITE)
    functionTextLeft = functionFont.render("the 'moveLeft()' function moves your character to the left",1,WHITE)
    functionTextUp = functionFont.render("the 'moveUp()' function moves your character upwards",1,WHITE)
    functionTextRightAgain = functionFont.render("the 'moveRightAgain()' function moves your character to the right again",1,WHITE)
    
    #continue text
    continueText = continueFont.render('Press The Space Bar To continue',1,WHITE)

    ##prompt
    gameDisplay.blit(promptText,[10,25])
    gameDisplay.blit(promptText2,[10,75])

    ##functions
    gameDisplay.blit(functionTextRight,[10,175])
    gameDisplay.blit(functionTextDown,[10,250])
    gameDisplay.blit(functionTextLeft,[10,325])
    gameDisplay.blit(functionTextUp,[10,400])
    gameDisplay.blit(functionTextRightAgain,[10,475])
    
    ##press to continue
    gameDisplay.blit(continueText,[10,575])

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()
