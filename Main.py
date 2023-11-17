import sys
import pygame
from Models.Fruit import Fruit
from Models.Snake import Snake

class Main:
    def __init__(self, cellNumber, cellSize, screen):
        self.fruit = Fruit(cellNumber)
        self.snake = Snake()
        self.cellNumber = cellNumber
        self.cellSize = cellSize
        self.screen = screen
        self.score = 0
        self.gameFont = pygame.font.Font('Fonts/Retro-Gaming.ttf', 25)
        
    def update(self):
        self.snake.move()
        self.checkCollision()
        self.checkFail()
    
    def draw(self):
        self.drawGrass()
        self.drawElements()
        self.drawScore()
    def drawElements(self):
        self.fruit.draw(self.cellSize, self.screen)
        self.snake.draw(self.cellSize, self.screen)
    def drawGrass(self):
        grassColor = (167,209,61)
        for row in range(self.cellNumber):
            if row%2 == 0:
                for col in range(self.cellNumber):
                    if col %2 == 0:
                        grassRect = pygame.Rect(col*self.cellSize, row* self.cellSize, self.cellSize, self.cellSize)
                        pygame.draw.rect(self.screen, grassColor, grassRect)
            else:
                for col in range(self.cellNumber):
                    if col %2 != 0:
                        grassRect = pygame.Rect(col*self.cellSize, row* self.cellSize, self.cellSize, self.cellSize)
                        pygame.draw.rect(self.screen, grassColor, grassRect)
    def drawScore(self):
        scoreText = str(len(self.snake.body)-3)
        scoreSurface = self.gameFont.render(scoreText, False, (0, 0, 0))
        scoreX = int(self.cellSize*self.cellNumber - 60)
        scoreY = int(self.cellSize * self.cellNumber - 40)
        scoreRect = scoreSurface.get_rect(center = (scoreX, scoreY))
        fruitRect = self.fruit.sprite.get_rect(midright = (scoreRect.left, scoreRect.centery))
        bgRect = pygame.Rect(fruitRect.left, fruitRect.top, fruitRect.width + scoreRect.width + 8 ,fruitRect.height)
        pygame.draw.rect(self.screen, (167,209,61), bgRect)
        self.screen.blit(scoreSurface, scoreRect)
        self.screen.blit(self.fruit.sprite, fruitRect)
        pygame.draw.rect(self.screen,(0, 0, 0), bgRect, 2)
    
    def keyInput(self, event):
        self.snake.changeDirection(event)
        
    def checkCollision(self):        
        if(self.snake.body[0].x == self.fruit.pos.x and self.snake.body[0].y == self.fruit.pos.y):
            self.fruit.randomize(self.cellNumber)
            self.snake.addBlock()
    
    def checkFail(self):
        if not 0 <= self.snake.body[0].x < self.cellNumber or not 0 <= self.snake.body[0].y < self.cellNumber:
            self.reset()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.reset()
                
    def reset(self):
        print("Game Over")
        self.snake.reset()
    
    def gameOver(self):
        pygame.quit()
        sys.exit()