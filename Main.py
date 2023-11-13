import pygame, sys

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize*cellNumber, cellSize*cellNumber))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
    screen.fill((175,215,70))
