##Block Library

import pygame, sys
from pygame.locals import *

class Block(pygame.sprite.Sprite):

    def __init__(self, surf, item, pos, size, theme):
        pygame.sprite.Sprite.__init__(self)

        self.surf = surf
        #self.block = pygame.Surface((size[0], size[1]))
        self.image = self.__getImage(item, theme)
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def displayBlock(self):
        self.surf.blit(self.image, self.rect)

    def __getImage(self, item, theme):
        if item == 'x':
            if theme == 'christmas':
                return pygame.image.load('Sprites//christmas block.png')
            if theme == 'halloween':
                return pygame.image.load('Sprites//halloween block.png')
            if theme == 'valentines':
                return pygame.image.load('Sprites//valentines block.png')
            if theme == 'easter':
                return pygame.image.load('Sprites//easter block.png')
            if theme == 'patricks':
                return pygame.image.load('Sprites//StPatricks block.png')
            if theme == 'thanksgiving':
                return pygame.image.load('Sprites//thanksgiving.png')
            else:
                return pygame.image.load('Sprites//basicBlock.png')
        if item == 'p':
            return pygame.image.load('Sprites//basicPlayer.png')
        if item == 'd':
            return pygame.image.load('Sprites//door.png')
        if item == 'e':
            return pygame.image.load('Sprites//enemy.png')        
        if item == 'c':
            return pygame.image.load('Sprites//coin.png')
        else:
            return pygame.image.load('Sprites//error.png')
