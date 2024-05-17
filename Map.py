import pygame
from Player import player
#from NPC import Npc
#from NPC2 import Npc2
from Fire_Ball import fireball
from Enemy import enemy 
pygame.init()
pygame.display.set_caption("Top down Grid Game") # Window Title
screen = pygame.display.set_mode((500,500)) # Game Screen
clock = pygame.time.Clock()
gameover = False
ticker = 0 
#player instantiation
p1 = player()
e1 = enemy()
ball = fireball()
#Player Constants
LEFT = 0 
RIGHT = 1 
UP = 2 
DOWN = 3 
SPACE = 4 
W = 5
keys = [False,False,False,False,False]

map = [[2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,2],
       [2,1,1,1,1,2,2,1,1,2],
       [2,1,1,2,2,2,2,1,1,2],
       [2,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('brick.png')
grass = pygame.image.load('grass.png')

while not gameover: #Game loop######
    clock.tick(60) #FPS
    ticker+=1 
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
        
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
    #physics------------------------------
    p1.move(keys,map)  
    if keys [SPACE] == True: 
        ball.shoot(p1.xpos,p1.ypos, p1.direction)
    if ball.isAlive == True: 
        ball.move()
    e1.move(map, ticker, p1.xpos,p1.ypos)
    #render section------------------------
    
    screen.fill((0,0,0)) #Screen Wipe
    #Draw map 
    for i in range (10):
        for j in range(10):
            if map[i][j] == 1:
                screen.blit(grass,(j * 50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick,(j * 50, i * 50), (0, 0, 50, 50))    
    p1.draw(screen)
    e1.draw(screen)
    #draw fireball 
    if ball.isAlive == True: 
        ball.draw(screen)
    pygame.display.flip()                
                
#end game loop-----------------------------------------------------
pygame.quit()






