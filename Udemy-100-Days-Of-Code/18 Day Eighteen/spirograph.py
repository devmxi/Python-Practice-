from turtle import Turtle, Screen
import turtle as t 
import random

t.colormode(255)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return  (r, g, b)

mxi = Turtle()
mxi.shape("turtle")
mxi.speed(0)

def spirograph(gap_size):
    for x in range(360 // gap_size):
        mxi.circle(100)
        mxi.setheading(mxi.heading() + gap_size)
        mxi.color(rand_color())

spirograph(5)
    
    
screen = Screen()
screen.exitonclick()