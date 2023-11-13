import pygame, sys
from Fruit import Fruit

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize*cellNumber, cellSize*cellNumber))
clock = pygame.time.Clock()

fruit = Fruit(cellNumber, cellSize, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
    screen.fill((175,215,70))
    fruit.drawFruit()
