from turtle import Turtle, Screen
mxi = Turtle()
screen = Screen()
 
def move_forward():
    mxi.forward(10)
    
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.exitonclick()