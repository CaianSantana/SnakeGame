import pygame, sys
from Models.Fruit import Fruit
from Models.Snake import Snake
from pygame.math import Vector2
pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize*cellNumber, cellSize*cellNumber))
clock = pygame.time.Clock()

fruit = Fruit(cellNumber)
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move()
        if event.type == pygame.KEYDOWN:
            snake.changeDirection(event.key)
    screen.fill((175,215,70))
    fruit.draw(cellSize, screen)
    snake.draw(cellSize, screen)
    pygame.display.update()
    clock.tick(60)
    