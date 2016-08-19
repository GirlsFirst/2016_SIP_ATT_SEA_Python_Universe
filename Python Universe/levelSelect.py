"""
 Python Universe
 Jisook & Malia
"""
#import stuff
import pygame
import random
import time
import sys
##from PIL import Image
from StarClass import Stars

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

##play music
pygame.mixer.music.load("Star Master Loop.wav")
pygame.mixer.music.play(50)


planet1 = pygame.image.load("bluePlanet.png")
planet2 = pygame.image.load("greenPlanet.png")
planet3 = pygame.image.load("lightPlanet.png")
planet4 = pygame.image.load("pinkPlanet.png")
planet5 = pygame.image.load("purplePlanet.png")
planet6 = pygame.image.load("redPlanet.png")

levelLocked = pygame.image.load("levelLocked.png")
level1 = pygame.image.load("lvl1.png")

##scale planets
scaleP1 = pygame.transform.scale(planet1, [160,160])
scaleP2 = pygame.transform.scale(planet2, [160,160])
scaleP3 = pygame.transform.scale(planet3, [160,160])
scaleP4 = pygame.transform.scale(planet4, [160,160])
scaleP5 = pygame.transform.scale(planet5, [160,160])
scaleP6 = pygame.transform.scale(planet6, [160,160])

lvlScale = pygame.transform.scale(levelLocked, [200,200])
lvl1 = pygame.transform.scale(level1, [200,200])


scaleP11 = pygame.transform.scale(planet1, [200,200])
scaleP22 = pygame.transform.scale(planet2, [200,200])
scaleP33 = pygame.transform.scale(planet3, [200,200])
scaleP44 = pygame.transform.scale(planet4, [200,200])
scaleP55 = pygame.transform.scale(planet5, [200,200])
scaleP66 = pygame.transform.scale(planet6, [200,200])

# Set the width and height of the screen [width, height]
size_width = (1366)
size_height = (900)
gameDisplay = pygame.display.set_mode((size_width,size_height))

pygame.display.set_caption("Python Universe")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Snow List
star_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 320 > mouse[0] > 195 and 336 > mouse[1] > 209:
                import levelOneDescription
                
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

    ##get mouse position
    mouse = pygame.mouse.get_pos()

    ##print mouse coordinates
    #print(mouse)

    
    ##display planets
    gameDisplay.blit(scaleP1,[171,198])
    gameDisplay.blit(scaleP2,[684,96])
    gameDisplay.blit(scaleP3,[1197,390])
    gameDisplay.blit(scaleP4,[855,550])
    gameDisplay.blit(scaleP5,[342,522])
    gameDisplay.blit(scaleP6,[684,390])






    if 320 > mouse[0] > 195 and 336 > mouse[1] > 209:
        gameDisplay.blit(scaleP11,(150,180))
        gameDisplay.blit(lvl1, (150,180))

    if 834 > mouse[0] > 708 and 232 > mouse[1] > 106:
        gameDisplay.blit(scaleP22,(664,76))
        gameDisplay.blit(lvlScale,[664,76])

    if 1348 > mouse[0] > 1221 and 526 > mouse[1] > 400:
        gameDisplay.blit(scaleP33,(1177,370))
        gameDisplay.blit(lvlScale,[1177,370])

    if 1006 > mouse[0] > 880 and 686 > mouse[1] > 560:
        gameDisplay.blit(scaleP44,(835,530))
        gameDisplay.blit(lvlScale,[835,530])

    if 492 > mouse[0] > 367 and 675 > mouse[1] > 515:
        gameDisplay.blit(scaleP55,(322,502))
        gameDisplay.blit(lvlScale,[322,502])

    if 834 > mouse[0] > 708 and 526 > mouse[1] > 401:
        gameDisplay.blit(scaleP66,(664,370))
        gameDisplay.blit(lvlScale,[664,370])


    
    ##display text    
    levelSelectFont = pygame.font.Font('mini_pixel-7.ttf', 100)    
    levelSelectText = levelSelectFont.render('Level Select',1,WHITE)
    gameDisplay.blit(levelSelectText, [100,50])

    
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
exit()

