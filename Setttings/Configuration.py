import pygame

cellSize = 40
cellNumber = 20
screenWidth = cellSize*cellNumber
screenHeight = cellSize*cellNumber


screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)