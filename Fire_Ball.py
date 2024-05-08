import pygame
#CONSTANTS
LEFT = 0 
RIGHT = 1 
UP = 2
DOWN = 3 
SPACE = 4 
W = 5

class fireball:  
    def __init__(self): 
        self.xpos = -10 
        self.ypos = -10 
        self.isAlive = False 
        self.direction = RIGHT 
    def shoot(self, x, y, dir):
        self.xpos = x + 20 
        self.ypos = y + 20 
        self.isAlive = True 
        self.direction = dir 


