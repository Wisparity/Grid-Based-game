import pygame
from Player import player
from NPC import Npc
from NPC2 import Npc2
pygame.init()
pygame.display.set_caption("Top down Grid Game") # Window Title
screen = pygame.display.set_mode((500,500)) # Game Screen
clock = pygame.time.Clock()
gameover = False

#player instantiation
p1 = player()

#Player Constants
LEFT = 0 
RIGHT = 1 
UP = 2 
DOWN = 3 
J = 4 
K = 5
R = 6
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
        
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
    #physics------------------------------
    p1.move(keys,map)  
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
    pygame.display.flip()                
                
#end game loop-----------------------------------------------------
pygame.quit()






