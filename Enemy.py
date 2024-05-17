import pygame 
import random 
#CONSTANTS 
LEFT = 0 
RIGHT = 1 
UP = 2 
DOWN = 3 
class enemy:
    def __init__(self):
        #player variables 
        self.xpos = 400
        self.ypos = 200
        self.vx = 0
        self.vy = 0
        self.direction = LEFT
    def draw(self,screen):
        pygame.draw.rect(screen, (255,0,255), (self.xpos, self.ypos, 30,30))


    def move(self,map,ticker,px,py):
    #randomly wander
        if ticker % 40 == 0: # Determins how often they change direction
            num = random.randrange (0,3)
            if num == 0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            
            elif num ==2:
                self.direction = UP
            elif num == 3: 
                self.direction = DOWN

            #expand to include up and down
            
    #  check if player is in line of sight
        if abs(int(py/50) - int(self.ypos/50))<2: #check if player and enemy are in same row
            if px < self.xpos: #check if the player is to the left of enemy
                self.xpos-=5
                self.direction = LEFT 
            else: 
                self.xpos+=5
                self.direction = RIGHT 


        #Collision check 

        #check right
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos + 25 ) / 50)] == 2:
            #print("Numped right")
            self.direction = LEFT
            self.xpos -= 6     

        #check left
        if self.direction == LEFT and map[int((self.ypos ) / 50)][int( (self.xpos - 5 ) / 50)] == 2:
            #print("Bumped left")
            self.direction = RIGHT
            self.xpos += 6 

        #check up
        if self.direction == UP and map[int((self.ypos-5 ) / 50)][int( (self.xpos ) / 50)] == 2:
            #print("Numped right")
            self.direction = DOWN
            self.ypos += 6     

        #checkdown
        if self.direction == DOWN and map[int((self.ypos+25 ) / 50)][int( (self.xpos ) / 50)] == 2:
            #print("Bumped left")
            self.direction = UP
            self.ypos -= 6 

        
        # Movement
        if self.direction == RIGHT: 
            self.xpos +=3 
        elif self.direction == LEFT:
            self.xpos -=3
        elif self.direction == UP:
            self.ypos -=3
        if self.direction == DOWN: 
            self.ypos +=3