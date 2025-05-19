from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

color_list = [(208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203)]
yvalue = -200 
xvalue = -200

mxi = Turtle()
mxi.shape("arrow")
mxi.color("black")
mxi.hideturtle()

mxi.up()
mxi.setpos(xvalue, yvalue)

for x in range(10):
    for x in range(10):
        mxi.dot(20, random.choice(color_list))
        mxi.penup()
        mxi.forward(50)
        
    yvalue += 50
    mxi.setpos(xvalue, yvalue)
    

screen.exitonclick()
