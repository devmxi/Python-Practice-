from turtle import Turtle, Screen

mxi = Turtle()
mxi.shape("turtle")
mxi.color("dark red")

for x in range(25):
    mxi.forward(10)
    mxi.penup()
    mxi.forward(10)
    mxi.pendown()

screen = Screen()
screen.exitonclick()