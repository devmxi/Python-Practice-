from turtle import Turtle, Screen
mxi = Turtle()
screen = Screen()

def move_forward():
    mxi.forward(10)

def move_backward():
    mxi.back(10)

def anticlockwise():
    mxi.left(10)

def clockwise():
    mxi.right(10)
    
def clear():
    mxi.penup()
    mxi.clear()
    mxi.home()
    mxi.pendown()

def movement(key_press, function):
    screen.onkey(key=key_press, fun=function)
    
screen.listen()

movement("w", move_forward)
movement("s", move_backward)
movement("a", anticlockwise)
movement("d", clockwise)
movement("c", clear)

screen.exitonclick()