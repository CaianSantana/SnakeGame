import pygame, sys
from Main import Main

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize*cellNumber, cellSize*cellNumber))
clock = pygame.time.Clock()

mainGame = Main(cellNumber, cellSize, screen)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            mainGame.keyInput(event.key)
    screen.fill((175,215,70))
    mainGame.draw()
    pygame.display.update()
    clock.tick(60)
    