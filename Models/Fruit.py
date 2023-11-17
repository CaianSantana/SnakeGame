import pygame, random
from pygame.math import Vector2

class Fruit:
    def __init__(self, cellNumber):
        self.randomize(cellNumber)
        self.rect = 0 
        self.sprite = pygame.image.load("Graphics/apple.png").convert_alpha()
          
    def randomize(self, cellNumber):
        self.x = random.randint(0, cellNumber-1)
        self.y = random.randint(0, cellNumber-1)
        self.pos = Vector2(self.x, self.y)

    def draw(self, cellSize, screen):
        self.rect = pygame.Rect(int(self.pos.x*cellSize),int(self.pos.y*cellSize), cellSize, cellSize)
        screen.blit(self.sprite, self.rect)