##Player Class

import pygame
from pygame.locals import *
import pyganim

class player(pygame.sprite.Sprite):
    
    def __init__(self, surf, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.pos = pos
        self.size = size
        self.__setCharacter()
        self.rect = Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        
        
    def setPosition(self, pos):
        self.pos = pos
    
    def setSize(self, size):
        self.size = size
        self.__setCharacter()
    
    def __setCharacter(self):
        self.front_standing = pygame.image.load('mygameimages/pro_front.png')
        self.front_standing = pygame.transform.scale(self.front_standing, (self.size[0], self.size[1]))
        self.back_standing = pygame.image.load('mygameimages/pro_back.png')
        self.back_standing = pygame.transform.scale(self.back_standing, (self.size[0], self.size[1]))
        self.right_standing = pygame.image.load('mygameimages/pro_right.png')
        self.right_standing = pygame.transform.scale(self.right_standing, (self.size[0], self.size[1]))
        self.left_standing = pygame.transform.flip(self.right_standing, True, False)
        
        self.playerWidth, self.playerHeight = self.front_standing.get_size()
        
        animTypes = 'back_run back_walk front_run front_walk right_run right_walk'.split()
        self.animObjs = {}
        for animType in animTypes:
            imagesAndDurations = [('mygameimages/pro_%s.%s.png' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
        
        self.animObjs['left_walk'] = self.animObjs['right_walk'].getCopy()
        self.animObjs['left_walk'].flip(True, False)
        self.animObjs['left_walk'].makeTransformsPermanent()
        self.animObjs['left_run'] = self.animObjs['right_run'].getCopy()
        self.animObjs['left_run'].flip(True, False)
        self.animObjs['left_run'].makeTransformsPermanent()
        
        self.moveConductor = pyganim.PygConductor(self.animObjs)
        self.moveConductor.scale((self.size[0], self.size[1]))        
    
    def getPlayerRect(self):
        self.rect = Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])