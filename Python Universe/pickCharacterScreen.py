import pygame
import random
#from pygame.locals import*
from StarClass import Stars


#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

#open images
guy = pygame.image.load("newboi.gif")
lady = pygame.image.load("malia.gif")
    
size_width = 1366
size_height = 768

gameDisplay = pygame.display.set_mode((size_width,size_height))

scaledGuy = pygame.transform.scale(guy,(256,256))
bigScaledGuy = pygame.transform.scale(guy,(320,320))
scaledLady = pygame.transform.scale(lady,(256,256))
bigScaledLady = pygame.transform.scale(lady,(320,320))

pygame.display.set_caption("Python Universe")

done = False

###play music
##pygame.mixer.music.load("8-bit Detective.wav")
##pygame.mixer.music.play(50)


clock = pygame.time.Clock()

star_list = []


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 384 > mouse[0] > 273 and 550 > mouse[1] > 322:
                import levelSelect
                
            if 977 > mouse[0] > 880 and 548 > mouse[1] > 373:
                import levelSelectGirl
              
        
    gameDisplay.fill(BLACK)
    
    randomX = random.randint (0,1350)
    randomY = random.randint (0,750)
    randomSize = random.randint (1,2)
    speed = random.randint (1,2)

    ##make stars   
    star_list.append(Stars(gameDisplay, WHITE, [randomX, randomY], speed, randomSize)) 
    for i in star_list:
        i.draw()
        i.fall()
    
    #display scaled characters
    gameDisplay.blit(scaledGuy,(200,300))
    gameDisplay.blit(scaledLady,(800,300))

    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    
    if 384 > mouse[0] > 273 and 550 > mouse[1] > 322:
        gameDisplay.blit(bigScaledGuy,(170,270))

    if 977 > mouse[0] > 880 and 548 > mouse[1] > 373:
        gameDisplay.blit(bigScaledLady,(770,265))
        
    # Display some text
    startFont = pygame.font.Font('mini_pixel-7.ttf', 100)
    text = startFont.render("Pick Your Character", 1, (255,255,255))
    gameDisplay.blit(text, [100,50]) 
    
    pygame.display.flip()

    ##60 fps
    clock.tick(60)

pygame.quit()
exit()

