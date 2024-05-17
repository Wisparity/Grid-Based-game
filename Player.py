import pygame
#player Constants
LEFT = 0 
RIGHT = 1 
UP = 2 
DOWN = 3 
J = 4 
K = 5
R = 6

class player:
    def __init__(self):
        #player variables 
        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0
        self.direction = LEFT

    def draw(self,screen):
        pygame.draw.rect(screen, (255,0,255), (self.xpos, self.ypos, 30,30))
    
    def move(self, keys, map):
        #Left Movement
        if keys[LEFT] == True:
            self.vx = -3
            self.direction = LEFT
            print("Moving Left")
        #Right Movement
        elif keys [RIGHT] == True:
            self.vx = 3 
            self.direction = RIGHT
            print("Moving Right")
        else:
            self.vx = 0 
        #Up Movement
        if keys [UP] == True:
            self.vy = -3
            self.direction = UP
            print("Moving Up")
        #Down Movement
        elif keys [DOWN] == True:
            self.vy = 3 
            self.direction = DOWN
            print("Moving Right")
        else: 
            self.vy = 0

        #Collision Physics
        #Left 
        if map[int((self.ypos) / 50)][int((self.xpos - 10)/ 50)] == 2: 
            self.xpos+=3
        
        #Right 
        if map[int((self.ypos) / 50)][int((self.xpos +30 +5) / 50)] == 2:
            self.xpos-=3
        #Up
        if map[int((self.ypos-5 ) / 50 )][int((self.xpos) / 50)] == 2:
            self.ypos+=3
        #Down 
        if map[int((self.ypos +35) / 50)][int((self.xpos) / 50)] == 2:
            self.ypos-=3
        self.xpos+=self.vx
        self.ypos+=self.vy
