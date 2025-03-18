from turtle import Turtle, Screen
import turtle as t 
import random

t.colormode(255)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return  (r, g, b)
    
angles = [0, 90, 180, 270, 360]

mxi = Turtle()
mxi.shape("turtle")
mxi.pensize(10)
mxi.speed(0)

for x in range(500):
    mxi.forward(15)
    mxi.right(random.choice(angles))
    color = rand_color()
    mxi.color(color)

screen = Screen()
screen.exitonclick()