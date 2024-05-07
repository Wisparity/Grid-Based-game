import pygame 
import random
import math 
LEFT = 0
RIGHT = 1
UP = 2 
DOWN = 3 

class Npc2: 
    def __init__(self):
        self.xpos = 400
        self.ypos = 200
        self.direction = RIGHT 
        self.isAlive = True

    def draw(self, screen):
        if self.isAlive == True: 
            pygame.draw.circle(screen, (0,0,240), (self.xpos, self.ypos), 20)

    def move(self, map, ticker, px, py):

        #randomly wander:
        if ticker % 40 == 0: 
            num = random.randrange(0,4)