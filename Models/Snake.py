import pygame, random
from pygame.math import Vector2

class Snake:
    def __init__(self, ):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        
    def drawSnake(self, cellSize, screen):
        for block in self.body:
            xPos = int(block.x*cellSize)
            yPos = int(block.y*cellSize)
            snakeRect = pygame.Rect(xPos, yPos, cellSize, cellSize)
            pygame.draw.rect(screen, ('green'), snakeRect)