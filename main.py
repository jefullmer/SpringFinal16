##Main

import pygame,sys
from pygame.locals import *

from bridgeClass import bridge
from menuClass import menu

pygame.mixer.pre_init(44100, -16, 2, 1024*4)
pygame.init()

clock = pygame.time.Clock()
FPS = 30
info = pygame.display.Info()
sWidth = info.current_w
sHeight = info.current_h
screen = pygame.display.set_mode((sWidth, sHeight), FULLSCREEN)
bgColor = (34, 53, 127)
screen.fill(bgColor)
pygame.display.set_caption("Final")
gameSong = pygame.mixer.Sound("Audio//game song.wav")

level = 1
MAX_LEVEL = 6
MIN_LEVEL = 1

UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'


gamePlay = bridge(screen, MIN_LEVEL, MAX_LEVEL)
mainMenuScreen = menu(screen)
mainMenuScreen.makeButton((int(sWidth * .5), int(sHeight * .083)), pygame.image.load('Sprites//start.png'), [int(sWidth * .25), int(sHeight * .416)])
mainMenuScreen.makeButton((int(sWidth * .5), int(sHeight * .083)), pygame.image.load('Sprites//exit.png'), [int(sWidth * .25), int(sHeight * .583)])
mainMenuScreen.makeText((sWidth, int(sHeight * .25)), 'Attack of the Holidays!', [0,0], (255,255,255))
mainMenuScreen.makeText((int(sWidth * .375), int(sHeight * .15)), 'By: Robotic Echo', [int(sWidth * .09375),int(sHeight * .833)], (69,107,255))

pauseScreen = menu(screen)
pauseScreen.makeText((int(sWidth * .5), int(sHeight * .25)), 'Pause', [int(sWidth * .25),0], (255,255,255))

overWorld = menu(screen)
overWorld.makeText((int(sWidth * .125), int(sHeight * .083)), 'Time: 0', [int(sWidth * .03215), int(sHeight * .0416)], (255,165,0))
overWorld.makeText((int(sWidth * .125), int(sHeight * .083)), 'Coins: 0', [int(sWidth * .03215), int(sHeight * .125)], (255,165,0))
overWorld.makeText((int(sWidth * .125), int(sHeight * .083)), 'Goal: 0', [int(sWidth * .03215), int(sHeight * .2083)], (255,165,0))

instructions = menu(screen)
instructions.makeText((sWidth, int(sHeight * .25)), 'Instructions',[0,0], (255, 255, 255))
instructions.makeText((int(sWidth * .4375), int(sHeight * .083)), 'Push the spacebar to continue', [int(sWidth * .25),int(sHeight * .833)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('W: Up'), [int(sWidth * .125),int(sHeight * .416)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('A: Left'), [int(sWidth * .125),int(sHeight * .4583)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('S: Down'), [int(sWidth * .125),int(sHeight * .5)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('D: Right'), [int(sWidth * .125),int(sHeight * .5416)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('Shift: Run'), [int(sWidth * .125),int(sHeight * .5833)], (255,255,255))
instructions.makeText((int(sWidth * .1875), int(sHeight * .066)), ('Goal:'), [int(sWidth * .375),int(sHeight * .416)], (255,255,255))
instructions.makeText((int(sWidth * .59375), int(sHeight * .066)), ('Collect Coins to progress to the next level.'), [int(sWidth * .375),int(sHeight * .4666)], (255,255,255))
instructions.makeText((int(sWidth * .59375), int(sHeight * .066)), ('Time will continue to countdown until you'), [int(sWidth * .375),int(sHeight * .516)], (255,255,255))
instructions.makeText((int(sWidth * .59375), int(sHeight * .066)), ('reach the end. Game is over when the timer'), [int(sWidth * .375),int(sHeight * .566)], (255,255,255))
instructions.makeText((int(sWidth * .59375), int(sHeight * .066)), ('ends or you reach the last level. Avoid the'), [int(sWidth * .375),int(sHeight * .616)], (255,255,255))
instructions.makeText((int(sWidth * .59375), int(sHeight * .066)), ('bouncing enemies, they take away time and'), [int(sWidth * .375),int(sHeight * .666)], (255,255,255))
instructions.makeText((int(sWidth * .46875), int(sHeight * .066)), ('reset the level. Good Luck!'), [int(sWidth * .375),int(sHeight * .716)], (255,255,255))

gameOver = menu(screen)
gameOver.makeText((sWidth, int(sHeight * .25)), 'GAME OVER!',[0,0], (255, 255, 255))
gameOver.makeText((int(sWidth * .625), int(sHeight * .083)), 'Push the spacebar to go to main menu', [int(sWidth * .125),int(sHeight * .666)], (255,255,255))
gameOver.makeText((int(sWidth * .625), int(sHeight * .083)), 'Push escape to close the game', [int(sWidth * .125),int(sHeight * .7416)], (255,255,255))
gameOver.makeText((int(sWidth * .625), int(sHeight * .083)), 'You Reached Level: 0', [int(sWidth * .125),int(sHeight * .333)], (255,255,255))

def gameOverScreen():
    gg = True
    gameOver.textList[3].changeText('You Reached Level: ' + str(gamePlay.currentLevel))
    if gamePlay.currentLevel > MAX_LEVEL:
        gameOver.textList[3].changeText('You Completed all ' + str(MAX_LEVEL) + ' levels!')
    while gg == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:        
                    gg = False      
        screen.fill(bgColor)
        
        gameOver.displayScreen()
        pygame.display.update()         
    main()

def mainMenu():
    menu = True
    while menu == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                 
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                if mainMenuScreen.buttonList[0].clicked(mouseXY):
                    menu = False
                if mainMenuScreen.buttonList[1].clicked(mouseXY):
                    pygame.quit()
                    sys.exit()                 
        screen.fill(bgColor)
        mainMenuScreen.displayScreen()
        pygame.display.update()        

def pauseMenu():
    pauseScreen.textList = []
    pauseScreen.makeText((int(sWidth * .5), int(sHeight * .25)), 'Pause', [int(sWidth * .25),0], (255,255,255))
    pauseScreen.makeText((int(sWidth * .25), int(sHeight * .083)), ('current Level: ' + str(gamePlay.currentLevel)), [int(sWidth * .125),int(sHeight * .416)], (255,255,255))
    pauseScreen.makeText((int(sWidth * .4375), int(sHeight * .083)), 'Push the spacebar to continue', [int(sWidth * .25),int(sHeight * .8333)], (255,255,255))
    pause = True
    while pause == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:        
                    pause = False               
        screen.fill(bgColor)
        pauseScreen.displayScreen()
        pygame.display.update()

def instructionMenu():
    menu = True
    while menu == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    menu = False
        screen.fill(bgColor)
        instructions.displayScreen()
        pygame.display.update()

def displayClock(seconds, count, go):
    count += 1
    if count >= FPS:
        seconds -= 1
        count = 0
    overWorld.textList[0].changeText('Time: ' + str(seconds))
    overWorld.displayScreen()
    if seconds <= 0:
        go = False
    return seconds, count, go
def scoreChange(newScore, goal, seconds):
    overWorld.textList[1].changeText('Coins: ' + str(newScore))
    overWorld.textList[2].changeText('Goal: ' + str(goal))
    overWorld.displayScreen()
    return seconds

def gameLoop():
    currentLevel = 1
    levelStr = ('Levels\lvl ' + str(currentLevel) + '.txt')
    speed = 5.0
    runSpeed = 7.0
    running = moveUp = moveDown = moveLeft = moveRight = False
    direction = DOWN
    count = 0
    go = True
    while go == True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key in (K_LSHIFT, K_RSHIFT):
                    running = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_w:
                    moveUp = True
                    moveDown = False
                    if not moveLeft and not moveRight:
                        direction = UP
                elif event.key == K_s:
                    moveDown = True
                    moveUp = False
                    if not moveLeft and not moveRight:
                        direction = DOWN
                elif event.key == K_a:
                    moveLeft = True
                    moveRight = False
                    if not moveUp and not moveDown:
                        direction = LEFT
                elif event.key == K_d:
                    moveRight = True
                    moveLeft = False
                    if not moveUp and not moveDown:
                        direction = RIGHT                
            elif event.type == KEYUP:
                #if event.key == pygame.K_UP:
                    #gamePlay.currentLevel = gamePlay.levelChange(gamePlay.currentLevel, 1)
                #elif event.key == pygame.K_DOWN:
                    #gamePlay.currentLevel = gamePlay.levelChange(gamePlay.currentLevel, -1)
                if event.key == pygame.K_SPACE:
                    running = moveUp = moveDown = moveLeft = moveRight = False
                    pauseMenu()                
                if event.key in (K_LSHIFT, K_RSHIFT):
                    running = False

                if event.key == K_w:
                    moveUp = False
                    if moveLeft:
                        direction = LEFT
                    if moveRight:
                        direction = RIGHT
                elif event.key == K_s:
                    moveDown = False
                    if moveLeft:
                        direction = LEFT
                    if moveRight:
                        direction = RIGHT
                elif event.key == K_a:
                    moveLeft = False
                    if moveUp:
                        direction = UP
                    if moveDown:
                        direction = DOWN
                elif event.key == K_d:
                    moveRight = False
                    if moveUp:
                        direction = UP
                    if moveDown:
                        direction = DOWN
        
        #pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_SPACE]:
            #gamePlay.loadLevel(gamePlay.currentLevel)
               
        
        screen.fill(bgColor)
        gamePlay.displayBlocks()
        gamePlay.movePlayer(speed, runSpeed, direction, running, moveUp, moveDown, moveLeft, moveRight)
        gamePlay.seconds, count, go = displayClock(gamePlay.seconds, count, go)
        gamePlay.seconds = scoreChange(gamePlay.currentCoins, gamePlay.goalCoins, gamePlay.seconds)
        
        if gamePlay.currentLevel > MAX_LEVEL:
            go = False
        clock.tick(FPS)
        pygame.display.update()
    
def main():
    gameSong.play(-1, 0)
    mainMenu()
    instructionMenu()
    gamePlay.loadLevel(level)
    gameLoop()
    gameOverScreen()

main()
