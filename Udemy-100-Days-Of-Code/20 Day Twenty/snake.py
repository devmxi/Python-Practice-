import time
from turtle import Turtle, Screen

MOVEMENT_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:
    def __init__(self):
        self.xvalue = 0
        self.yvalue = 0
        self.segments = []  
        self.create()
        
    def create(self):
        for x in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.color("white") 
            new_turtle.penup()
            self.xvalue -= 20
            new_turtle.goto(self.xvalue, 0)
            self.segments.append(new_turtle)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.xvalue = self.segments[seg -1].xcor()
            self.yvalue = self.segments[seg -1].ycor()
            self.segments[seg].goto(self.xvalue, self.yvalue)

        self.segments[0].forward(MOVEMENT_STEPS)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)