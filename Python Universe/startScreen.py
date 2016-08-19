"""
 Python Universe
 Jisook & Malia
"""
#import stuff
import pygame
import random
import time
import sys
from PIL import Image
from StarClass import Stars

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

#play music
pygame.mixer.music.load("8-bit Detective.wav")
pygame.mixer.music.play(50)

# Set the width and height of the screen [width, height]
size_width = (1366)
size_height = (768)
gameDisplay = pygame.display.set_mode((size_width,size_height))

pygame.display.set_caption("Python Universe")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Star List
star_list = []


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                import pickCharacterScreen
        
    gameDisplay.fill(BLACK)

##random variables
    randomX = random.randint (0,1350)
    randomY = random.randint (0,750)
    randomSize = random.randint (1,2)
    speed = random.randint (1,2)

    star_list.append(Stars(gameDisplay,WHITE, [randomX, randomY], speed, randomSize)) 
    for i in star_list:
        i.draw()
        i.fall()
        
     # Display some text 
    titleFont = pygame.font.Font('mini_pixel-7.ttf', 100)
    startFont = pygame.font.Font('mini_pixel-7.ttf',75)
    
    startText = startFont.render('Press Space To Start',1,WHITE)
    titleText = titleFont.render("PYTHON UNIVERSE", 1, WHITE)
    
    gameDisplay.blit(titleText, [100,50])
    gameDisplay.blit(startText,[100,300])
    
##    text_display("Press Space To Play")
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit() 


