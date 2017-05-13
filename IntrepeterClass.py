##IntrepeterClass

import pygame,sys
from pygame.locals import *

from blockLibrary import Block
from random import randint

class convert(object):

    def __init__(self, surf):

        self.screen = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        self.blockObjList = []
        self.blockXpos = []
        self.blockYpos = []        
        self.enemyList = []
        self.enemySpeed = []
        self.coinList = pygame.sprite.Group()
        self.coinNum = 0
        self.areEnemies = False

    def lvlConv(self, currentLvl):
        objFile = open(currentLvl, "r")
        self.clearBlocks()

        lineCount = 0
        tempList = []
        count = 0
        xPos = 0
        yPos = 0
        gridX = 0
        gridY = 0
        blockSize = [0,0]
        coinSize = [0,0]
        coinOffset = [0,0]
        self.playerSize = [0,0]
        player = 0
        door = 0
        self.areEnemies = False
        
        for line in objFile:
            lineCount += 1
            xPos = 0
            if lineCount == 1:
                tempList = line.split()
                tempList.remove('x')
                gridX = int(tempList[0])
                gridY = int(tempList[1])
                blockSize[0] = self.sWidth//gridX
                blockSize[1] = self.sHeight//gridY
                coinSize[0] = int(self.sWidth * .1)//gridX
                coinSize[1] = int(self.sWidth * .2)//gridY
                coinOffset[0] = blockSize[0]//2 - coinSize[0]//2
                coinOffset[1] = blockSize[1]//2 - coinSize[1]//2
                yPos -= blockSize[1]
            elif lineCount == 2:
                playerS = line.split()                
                if playerS[0] == 'dynamic':
                    self.playerSize[0] = int(self.sWidth * .1875)//gridX
                    self.playerSize[1] = int(self.sWidth * .3333)//gridY
                    xOff = blockSize[0]//4
                    yOff = (blockSize[1] - self.playerSize[1])
                elif playerS[0] == 'fixed':
                    self.playerSize[0] = 100
                    self.playerSize[1] = 150
                    xOff = 0
                    yOff = blockSize[1] - self.playerSize[1]
                yPos -= blockSize[1]
            elif lineCount == 3:
                eList = line.split()
                if eList[0] != 'none':
                    eList.remove('x')
                    self.areEnemies = True
                    for i in range(int(eList[0])):
                        self.enemyList.append(Block(self.screen, 'e', (0,0), blockSize, 'e'))
                        speedX = randint(-int(eList[1]), int(eList[1]))
                        speedY = randint(-int(eList[2]), int(eList[2]))
                        if speedX == 0:
                            speedX = 1
                        if speedY == 0:
                            speedY = 1
                        self.enemySpeed.append([speedX, speedY])
                yPos -= blockSize[1]
            elif lineCount == 4:
                theme = line.split()
                yPos -= blockSize[1]
            elif line[0] != '.':
                tempList = line.split()
                for item in tempList:
                    if item == 'x':                        
                        self.blockXpos.append(xPos)
                        self.blockYpos.append(yPos)
                        self.blockObjList.append(Block(self.screen, item, (xPos, yPos), blockSize, theme[0]))                        
                    elif item == 'c':
                        self.blockXpos.append(xPos)
                        self.blockYpos.append(yPos)
                        self.coinList.add(Block(self.screen, item, (xPos + coinOffset[0], yPos + coinOffset[1]), coinSize, 'c'))
                        self.coinNum = len(self.coinList)
                    elif item == 'p':
                        self.pXPos = xPos + xOff
                        self.pYPos = yPos + yOff
                        self.blockXpos.append(xPos)
                        self.blockYpos.append(yPos)
                    elif item == 'd':                        
                        self.blockXpos.append(xPos)
                        self.blockYpos.append(yPos)
                        self.door = Block(self.screen, item, (xPos, yPos), blockSize, 'd')
                        for x in self.enemyList:
                            x.rect.x = xPos
                            x.rect.y = yPos
                    xPos += blockSize[0]
            yPos += blockSize[1]
    def displayBlocks(self, blockList):
        for x in blockList:
            x.displayBlock()
    def clearBlocks(self):
        self.blockObjList.clear()
        self.enemyList.clear()
        self.enemySpeed.clear()
        self.coinList.empty()
        self.coinNum = 0
    def moveEnemyBlocks(self):
        if self.areEnemies:
            for i in range(len(self.enemyList)):
                self.enemyList[i].rect.x += self.enemySpeed[i][0]
                self.enemyList[i].rect.y += self.enemySpeed[i][1]
                if self.enemyList[i].rect.x < 0 or self.enemyList[i].rect.right > self.sWidth:
                    self.enemySpeed[i][0] = -self.enemySpeed[i][0]
                if self.enemyList[i].rect.y < 0 or self.enemyList[i].rect.bottom > self.sHeight:
                    self.enemySpeed[i][1] = -self.enemySpeed[i][1]            
