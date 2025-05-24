from turtle import Turtle

class Gui(Turtle): 
    
    #gui set up
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.pensize(5)
        self.goto(-200, 500)
        self.setheading(270)
        self.pendown()
        self.forward(1000)
        self.penup()
        self.goto(200, 500)
        self.pendown()
        self.forward(1000)
        self.penup()
        self.goto(-300, 450)
        self.write("Next Up:", font=("Courier", 20), align= "center") #write next up 
        self.goto(0, 450)
        self.write("Tetris", font=("Courier", 20), align= "center") #write title 
        self.goto(300, 450)
        self.write("Score: ", font=("Courier", 20), align= "center") #write score 