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
    
    def draw(self):
        self.fruit.draw(self.cellSize, self.screen)
        self.snake.draw(self.cellSize, self.screen)
    
    def keyInput(self, event):
        self.snake.changeDirection(event)
        
    def checkCollision(self):
        if(self.fruit.Rect.colliderect(self.snake.Rect)):
            self.fruit.reset(self.cellNumber)
            
            bodyCopy = self.snake.body[:]
            bodyCopy.insert(0,bodyCopy[0]+self.snake.direction)
            self.snake.body = bodyCopy[:]