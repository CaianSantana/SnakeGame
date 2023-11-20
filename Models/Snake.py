import pygame, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(0,0)
        self.rect = 0
        
        self.headLeft = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.headRight = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.headUp = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.headDown = pygame.image.load("Graphics/head_down.png").convert_alpha()
        
        self.bodyBottomLeft = pygame.image.load("Graphics/body_bottomleft.png").convert_alpha()
        self.bodyBottomRight = pygame.image.load("Graphics/body_bottomright.png").convert_alpha()
        self.bodyTopLeft = pygame.image.load("Graphics/body_topleft.png").convert_alpha()
        self.bodyTopRight = pygame.image.load("Graphics/body_topright.png").convert_alpha()
        self.bodyHorizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.bodyVertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        
        
        self.tailLeft = pygame.image.load("Graphics/tail_left.png").convert_alpha()
        self.tailRight = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        self.tailUp = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tailDown = pygame.image.load("Graphics/tail_down.png").convert_alpha()

    def draw(self, cellSize, screen):
        self.updateHeadGraphics()
        self.updateTailGraphics()
        
        for index, block in enumerate(self.body):
            
           # self.chest = self.updateChestGraphics(index)
            
            
            xPos = int(block.x*cellSize)
            yPos = int(block.y*cellSize)
            self.rect = pygame.Rect(xPos, yPos, cellSize, cellSize)
    
            if index==0:
                screen.blit(self.head, self.rect)
            elif block == self.body[-1]:
                screen.blit(self.tail, self.rect)
            else:
                previousBlock = self.body[index+1] - block
                nextBlock = self.body[index-1] - block
                if previousBlock.x == nextBlock.x:
                    screen.blit(self.bodyVertical, self.rect)
                elif previousBlock.y == nextBlock.y:
                    screen.blit(self.bodyHorizontal, self.rect)
                else:
                    if previousBlock.x == -1 and nextBlock.y == -1 or  previousBlock.y == -1 and nextBlock.x ==-1:
                        screen.blit(self.bodyTopLeft, self.rect)
                    elif previousBlock.x == -1 and nextBlock.y == 1 or  previousBlock.y == 1 and nextBlock.x ==-1:
                        screen.blit(self.bodyBottomLeft, self.rect)
                    elif previousBlock.x == 1 and nextBlock.y == -1 or  previousBlock.y == -1 and nextBlock.x ==1:
                        screen.blit(self.bodyTopRight, self.rect)
                    else:
                        screen.blit(self.bodyBottomRight, self.rect)
    
    def updateHeadGraphics(self):
        headRelation = self.body[1] - self.body[0]
        if headRelation == Vector2(1,0):
            self.head = self.headLeft
        elif headRelation == Vector2(-1,0):
            self.head = self.headRight
        elif headRelation == Vector2(0,-1):
            self.head = self.headDown
        else:
            self.head = self.headUp
        
    
    def updateTailGraphics(self):
        tailRelation = self.body[-1] - self.body[-2]
        if tailRelation == Vector2(1,0):
            self.tail = self.tailRight
        elif tailRelation == Vector2(-1,0):
            self.tail = self.tailLeft
        elif tailRelation == Vector2(0,-1):
            self.tail = self.tailUp
        else:
            self.tail = self.tailDown 
        
    def move(self):
        if not self.direction.x == 0 or not self.direction.y == 0:
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0,bodyCopy[0]+self.direction)
            self.body = bodyCopy[:]
        
    def changeDirection(self, event):
        match event:
            case pygame.K_UP:
                if not self.direction.y == 1:
                    self.direction = Vector2(0,-1)
            case pygame.K_DOWN:
                if not self.direction.y == -1:
                    self.direction = Vector2(0,1)
            case pygame.K_RIGHT:
                if not self.direction.x == -1:
                    self.direction = Vector2(1,0)
            case pygame.K_LEFT:
                if not self.direction.x == 1:
                    self.direction = Vector2(-1, 0)
    
    def addBlock(self):
        bodyCopy = self.body[:]
        bodyCopy.insert(0,bodyCopy[0]+self.direction)
        self.body = bodyCopy[:]
        
    def reset(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(0,0)