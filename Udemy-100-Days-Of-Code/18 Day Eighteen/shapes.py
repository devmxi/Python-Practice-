from turtle import Turtle, Screen
import random

colors = ["dark red", "blue", "green", "pink", "cyan", "black"]

mxi = Turtle()
mxi.shape("turtle")
mxi.color("dark red")

for x in range(3, 11):
    mxi.color(random.choice(colors))
    angle = 360/x
    for loop in range(x):
        mxi.forward(100)
        mxi.right(angle)
    
screen = Screen()
screen.exitonclick()