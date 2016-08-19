#button class
import pygame
from pygame.locals import *
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Button():

    def __init__(self,screen,width,height,button_color,text_color,font,text):
        #initialize button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions and properties of the button
        self.width, self.height = 200,50
        self.button_color = WHITE
        self.text_color = BLACK
        self.font = ("mini_pixel-7.ttf")
        self.text = text

        #build button's rect object
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #button message needs to be prepped only once
        self.prep_msg(text)

    def prep_msg(self,text):
        #turn text into rendered image and center it on button
        self.text_image = self.font.render(text,True,self.text_color,
                                           self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect_center

    def draw_button(self):
        #draw blank button and then draw message
        self.gameDisplay.fill(self.button_color,self.rect)
        self.gameDisplay.blit(self.text_image,self.text_image_rect)















    
