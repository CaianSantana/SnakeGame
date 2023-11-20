from Setttings.Main import Main
from Setttings.Configuration import screen, pygame, clock, SCREEN_UPDATE

pygame.init()
mainGame = Main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            mainGame.keyInput(event.key)
    screen.fill((175,215,70))
    mainGame.draw()
    pygame.display.update()
    clock.tick(60)
    