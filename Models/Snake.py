import pygame, random
from pygame.math import Vector2

class Snake:
    def __init__(self, ):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
        
    def draw(self, cellSize, screen):
        for block in self.body:
            xPos = int(block.x*cellSize)
            yPos = int(block.y*cellSize)
            snakeRect = pygame.Rect(xPos, yPos, cellSize, cellSize)
            pygame.draw.rect(screen, ('green'), snakeRect)
    def move(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0,bodyCopy[0]+self.direction)
        self.body = bodyCopy[:]
    def changeDirection(self, event):
        match event:
            case pygame.K_UP:
                self.direction = Vector2(0,-1)
            case pygame.K_DOWN:
                self.direction = Vector2(0,1)
            case pygame.K_RIGHT:
                self.direction = Vector2(1,0)
            case pygame.K_LEFT:
                self.direction = Vector2(-1, 0)
        
                
    