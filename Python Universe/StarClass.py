import pygame
import time
import random
import sys

class Stars():
    
    def __init__(self, gameDisplay, color, position, speed, size, wind=False):
        self.color = color
        self.position = position
        self.speed = speed
        self.size = size
        self.gameDisplay = gameDisplay
    
    def fall(self):
        self.position[1]-=self.speed
        
    def draw(self):        
        pygame.draw.circle(self.gameDisplay, self.color, self.position, self.size)


