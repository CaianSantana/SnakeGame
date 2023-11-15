import pygame, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(1,0)
        self.Rect = 0

    def draw(self, cellSize, screen):
        for block in self.body:
            xPos = int(block.x*cellSize)
            yPos = int(block.y*cellSize)
            self.Rect = pygame.Rect(xPos, yPos, cellSize, cellSize)
            pygame.draw.rect(screen, ('green'), self.Rect)
    def move(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0,bodyCopy[0]+self.direction)
        self.body = bodyCopy[:]
    def changeDirection(self, event):
        match event:
            case pygame.K_UP:
                if not self.direction.y == 1:
                    self.direction = Vector2(0,-1)
            case pygame.K_DOWN:
                if not self.direction.y == -1:
                    self.direction = Vector2(0,1)
            case pygame.K_RIGHT:
                if not self.direction.x == -1:
                    self.direction = Vector2(1,0)
            case pygame.K_LEFT:
                if not self.direction.x == 1:
                    self.direction = Vector2(-1, 0)
    
    def addBlock(self):
        bodyCopy = self.body[:]
        bodyCopy.insert(0,bodyCopy[0]+self.direction)
        self.body = bodyCopy[:]