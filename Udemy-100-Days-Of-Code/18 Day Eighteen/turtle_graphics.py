from turtle import Turtle, Screen

mxi = Turtle()
mxi.shape("turtle")
mxi.color("dark red")

for x in range(4):
    mxi.right(90)
    mxi.forward(100)

screen = Screen()
screen.exitonclick()