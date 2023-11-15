import pygame, random
from pygame.math import Vector2

class Fruit:
    def __init__(self, cellNumber):
        self.randomize(cellNumber)
        self.Rect = 0 
          
    def randomize(self, cellNumber):
        self.x = random.randint(0, cellNumber-1)
        self.y = random.randint(0, cellNumber-1)
        self.pos = Vector2(self.x, self.y)

    def draw(self, cellSize, screen):
        self.Rect = pygame.Rect(int(self.pos.x*cellSize),int(self.pos.y*cellSize), cellSize, cellSize)
        pygame.draw.rect(screen, ('red'), self.Rect)