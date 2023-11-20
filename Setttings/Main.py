import pygame
import sys
from Setttings.Configuration import cellNumber, cellSize, screen
from Models.Fruit import Fruit
from Models.Snake import Snake

class Main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()
        self.score = 0
        self.gameFont = pygame.font.Font('Fonts/Retro-Gaming.ttf', 25)
        
    def update(self):
        self.snake.move()
        self.checkCollision()
        self.checkFail()
    
    def draw(self):
        self.drawGrass()
        self.drawScore()
        self.drawElements()
  
    def drawElements(self):
        self.fruit.draw()
        self.snake.draw()
    def drawGrass(self):
        grassColor = (167,209,61)
        for row in range(cellNumber):
            if row%2 == 0:
                for col in range(cellNumber):
                    if col %2 == 0:
                        grassRect = pygame.Rect(col*cellSize, row* cellSize, cellSize, cellSize)
                        pygame.draw.rect(screen, grassColor, grassRect)
            else:
                for col in range(cellNumber):
                    if col %2 != 0:
                        grassRect = pygame.Rect(col*cellSize, row* cellSize, cellSize, cellSize)
                        pygame.draw.rect(screen, grassColor, grassRect)
    def drawScore(self):
        self.score = str(len(self.snake.body)-3)
        scoreText = self.score
        scoreSurface = self.gameFont.render(scoreText, False, (0, 0, 0))
        scoreX = int(cellSize*cellNumber - 60)
        scoreY = int(cellSize * cellNumber - 40)
        scoreRect = scoreSurface.get_rect(center = (scoreX, scoreY))
        fruitRect = self.fruit.sprite.get_rect(midright = (scoreRect.left, scoreRect.centery))
        bgRect = pygame.Rect(fruitRect.left, fruitRect.top, fruitRect.width + scoreRect.width + 8 ,fruitRect.height)
        pygame.draw.rect(screen, (167,209,61), bgRect)
        screen.blit(scoreSurface, scoreRect)
        screen.blit(self.fruit.sprite, fruitRect)
        pygame.draw.rect(screen,(0, 0, 0), bgRect, 2)
    
    def keyInput(self, event):
        self.snake.changeDirection(event)
        
    def checkCollision(self):        
        if(self.snake.body[0].x == self.fruit.pos.x and self.snake.body[0].y == self.fruit.pos.y):
            self.fruit.randomize()
            self.snake.addBlock()
        if not 0 <= self.snake.body[0].x < cellNumber:
            if self.snake.body[0].x == cellNumber:
                self.snake.body[0].x = 0 
                self.snake.changeDirection(pygame.K_RIGHT)
            else:
                self.snake.body[0].x = cellNumber-1  
                self.snake.changeDirection(pygame.K_LEFT)
        elif not 0 <= self.snake.body[0].y < cellNumber:
            if self.snake.body[0].y == cellNumber:
                self.snake.body[0].y = 0 
                self.snake.changeDirection(pygame.K_UP)
            else:
                self.snake.body[0].y = cellNumber-1  
                self.snake.changeDirection(pygame.K_DOWN)
            
    
    def checkFail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.reset()
                
    def reset(self):
        print("Game Over\nScore: "+ str(self.score))
        self.snake.reset()
    
    def gameOver(self):
        pygame.quit()
        sys.exit()