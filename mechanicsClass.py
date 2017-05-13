##Mechanics Class

import pygame, sys
from pygame.locals import *

class mechanic(object):
    
    def __init__(self, surf):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
    
    def blockCheck(self, rectIn, rect2, direction):
        if rectIn.colliderect(rect2):
            if rectIn.bottom >= rect2.top and direction == 'd':
                rectIn.bottom = rect2.top
            elif rectIn.top <= rect2.bottom and direction == 'u':
                rectIn.top = rect2.bottom 
            elif rectIn.left <= rect2.right and direction == 'l':
                rectIn.left = rect2.right    
            elif rectIn.right >= rect2.left and direction == 'r':
                rectIn.right = rect2.left            
        return rectIn
    def wallCheck(self, rect1, direction):
        if rect1.left < 0 and direction == 'l':
            rect1.left = 0
        if rect1.right > self.sWidth and direction == 'r':
            rect1.right = self.sWidth     
        if rect1.top < 0 and direction == 'u':
            rect1.top = 0
        if rect1.bottom > self.sHeight and direction == 'd':
            rect1.bottom = self.sHeight
        return rect1
    def collisionTrigger(self, rect1, rect2):
        return rect1.colliderect(rect2)