from turtle import Turtle
import random

class Food(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.randomx = random.randint(-260, 260)
        self.randomy = random.randint(-260, 260)
        self.goto(self.randomx, self.randomy)