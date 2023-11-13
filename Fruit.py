import pygame, random
from pygame.math import Vector2

class Fruit:
    def __init__(self, cellNumber, cellSize, screen):
        self.x = random.randint(0, cellNumber-1)
        self.y = random.randint(0, cellNumber-1)
        self.pos = Vector2(self.x, self.y)
        self.cellNumber = cellNumber
        self.cellSize = cellSize
        self.screen = screen
        
    def drawFruit(self):
        fruitRect = pygame.Rect(int(self.pos.x*self.cellSize),int(self.pos.y*self.cellSize), self.cellSize, self.cellSize)
        pygame.draw.rect(self.screen, (126, 166, 114), fruitRect)