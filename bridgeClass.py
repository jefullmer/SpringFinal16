##Bridge Class

import pygame, sys
from pygame.locals import *

from IntrepeterClass import convert
from mechanicsClass import mechanic
from playerClass import player

class bridge(object):
    
    def __init__(self, surf, minLvl, maxLvl):
        self.surf = surf
        self.MIN_LEVEL = minLvl
        self.MAX_LEVEL = maxLvl
        self.lvlConverter = convert(surf)
        self.mech = mechanic(surf)
        self.jumping = False
        self.gravity = 5.0
        self.pos0Y = 0
        self.time0 = 0
        self.currentLevel = 1
        self.hero = player(surf, [0,0], [0,0])
        self.currentCoins = 0
        self.goalCoins = 0
        self.seconds = 55
        
        self.coinSound = pygame.mixer.Sound("Audio//PickupCoin.wav")
    
    def levelChange(self, currLevel, direction):
        thisLevel = currLevel + direction
        if thisLevel > self.MAX_LEVEL:
            return thisLevel
        if thisLevel > self.MAX_LEVEL:
            thisLevel -= 1
        elif thisLevel < self.MIN_LEVEL:
            thisLevel += 1
        self.loadLevel(thisLevel)
        return thisLevel
    
    def loadLevel(self, level):
        lvlStr = ('Levels/lvl ' + str(level) + '.txt')
        self.lvlConverter.lvlConv(lvlStr)
        self.hero.setPosition([self.lvlConverter.pXPos, self.lvlConverter.pYPos])
        self.hero.setSize(self.lvlConverter.playerSize)
        self.hero.getPlayerRect()
        self.goalCoins = self.lvlConverter.coinNum
        self.currentCoins = 0
        self.seconds += 5
    
    def displayBlocks(self):
        self.lvlConverter.moveEnemyBlocks()
        self.lvlConverter.displayBlocks(self.lvlConverter.blockObjList)
        self.lvlConverter.displayBlocks(self.lvlConverter.coinList)
        self.lvlConverter.door.displayBlock()
        self.lvlConverter.displayBlocks(self.lvlConverter.enemyList)
        for x in self.lvlConverter.enemyList:
            if self.mech.collisionTrigger(self.hero.rect, x.rect):
                self.loadLevel(self.currentLevel)
                self.seconds -= 20
                #print('yes!') 
        collisionList = pygame.sprite.spritecollide(self.hero, self.lvlConverter.coinList, True)
        for col in collisionList:
            self.currentCoins += 1
            self.coinSound.play()
            self.seconds += 2
        

    def blockCheck(self, direction):
        self.hero.rect = self.mech.wallCheck(self.hero.rect, direction)
        if self.hero.rect.colliderect(self.lvlConverter.door.rect) and self.currentCoins == self.goalCoins:
            self.currentLevel = self.levelChange(self.currentLevel, 1)
        for x in self.lvlConverter.blockObjList:
            self.hero.rect = self.mech.blockCheck(self.hero.rect, x.rect, direction)
        
        
            
    def movePlayer(self, speed, runSpeed, direction, running, moveUp, moveDown, moveLeft, moveRight):
        if moveUp or moveDown or moveLeft or moveRight:
            self.hero.moveConductor.play()
            if running:
                if direction == 'u':
                    self.hero.animObjs['back_run'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'd':
                    self.hero.animObjs['front_run'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'l':
                    self.hero.animObjs['left_run'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'r':
                    self.hero.animObjs['right_run'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
            else:
                if direction == 'u':
                    self.hero.animObjs['back_walk'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'd':
                    self.hero.animObjs['front_walk'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'l':
                    self.hero.animObjs['left_walk'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
                if direction == 'r':
                    self.hero.animObjs['right_walk'].blit(self.surf, (self.hero.rect.x, self.hero.rect.y))
            if running:
                rate = runSpeed
            else:
                rate = speed
            if moveUp:
                self.hero.rect.y -= rate
                self.blockCheck('u')
            if moveDown:
                self.hero.rect.y += rate
                self.blockCheck('d')
            if moveLeft:
                self.hero.rect.x -= rate
                self.blockCheck('l')
            if moveRight:
                self.hero.rect.x += rate
                self.blockCheck('r')
        else:
            self.hero.moveConductor.stop()
            if direction == 'u':
                self.surf.blit(self.hero.back_standing, (self.hero.rect.x, self.hero.rect.y))
            elif direction == 'd':
                self.surf.blit(self.hero.front_standing, (self.hero.rect.x, self.hero.rect.y))            
            elif direction == 'l':
                self.surf.blit(self.hero.left_standing, (self.hero.rect.x, self.hero.rect.y))                
            elif direction == 'r':
                self.surf.blit(self.hero.right_standing, (self.hero.rect.x, self.hero.rect.y))            
           