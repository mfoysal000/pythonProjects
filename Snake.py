import pygame
import time
import random 

#The Mainframe
pygame.init()

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

disWidth = 600
disHeight = 400

display = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
snakeBlock = 10
snakeSpeed = 15

fontStyle = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("comicsansms", 35)

def theScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0,0])

def ourSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(display, black, [x[0], x[1], snakeBlock, snakeBlock])


def message(msg, color):
    mesg=fontStyle.render(msg, True, color)
    display.blit(mesg, [disWidth/12, disHeight/3])

def gameLoop():
    gameOver=False 
    gameClose=False

    x1 = disWidth/2
    y1 = disHeight/2
    x1change=0
    y1change=0

    snakeList = []
    LengthOfSnake = 1

    foodx = round(random.randrange(0, disWidth - snakeBlock)/10.0)*10.0
    foody = round(random.randrange(0, disWidth - snakeBlock)/10.0)*10.0

    while not gameOver:

        while gameClose == True:
            display.fill(blue)
            message("You lost! Press Q to quit or C to play again", red)
            theScore(LengthOfSnake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x1change=-snakeBlock
                    y1change=0
                elif event.key==pygame.K_d:
                    x1change=snakeBlock
                    y1change=0
                elif event.key==pygame.K_w:
                    y1change=-snakeBlock
                    x1change=0
                elif event.key==pygame.K_s:
                    y1change=snakeBlock
                    x1change=0
                elif event.key==pygame.K_LEFT:
                    x1change=-snakeBlock
                    y1change=0
                elif event.key==pygame.K_RIGHT:
                    x1change=snakeBlock
                    y1change=0
                elif event.key==pygame.K_UP:
                    y1change=-snakeBlock
                    x1change=0
                elif event.key==pygame.K_DOWN:
                    y1change=snakeBlock
                    x1change=0

        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True
        
        x1 += x1change
        y1 += y1change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx,foody,snakeBlock,snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > LengthOfSnake:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
        
        ourSnake(snakeBlock, snakeList)
        theScore(LengthOfSnake - 1)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disWidth - snakeBlock)/10.0)*10.0
            foody = round(random.randrange(0, disWidth - snakeBlock)/10.0)*10.0
            LengthOfSnake += 1
            print('Yummy!')
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()


