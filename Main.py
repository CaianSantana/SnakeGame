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
    
    def draw(self):
        self.fruit.draw(self.cellSize, self.screen)
        self.snake.draw(self.cellSize, self.screen)
    
    def keyInput(self, event):
        self.snake.changeDirection(event)