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
        
    def update(self):
        self.snake.move()
        self.checkCollision()
        self.checkFail()
    
    def draw(self):
        self.fruit.draw(self.cellSize, self.screen)
        self.snake.draw(self.cellSize, self.screen)
    
    def keyInput(self, event):
        self.snake.changeDirection(event)
        
    def checkCollision(self):
        if(self.fruit.Rect.colliderect(self.snake.Rect)):
            self.fruit.randomize(self.cellNumber)
            self.snake.addBlock()
    
    def checkFail(self):
        if not 0 <= self.snake.body[0].x < self.cellNumber or not 0 <= self.snake.body[0].y < self.cellNumber:
            self.gameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()
            
    def gameOver(self):
        print("Game Over")
        pygame.quit()
        sys.exit()