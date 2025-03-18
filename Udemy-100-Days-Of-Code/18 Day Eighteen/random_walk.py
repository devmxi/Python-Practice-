from turtle import Turtle, Screen
import random

colors = ["dark red", "blue", "green", "pink", "cyan", "black"]
angles = [0, 90, 180, 270, 360]

mxi = Turtle()
mxi.shape("turtle")
mxi.pensize(10)
mxi.speed(0)

for x in range(500):
    mxi.forward(15)
    mxi.right(random.choice(angles))
    mxi.color(random.choice(colors))

screen = Screen()
screen.exitonclick()