from turtle import Turtle

class Scoreboard(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", font=("Courier", 20), align= "center")
        
    def update(self): 
        self.clear()
        self.write(f"Score: {self.score}", font=("Courier", 20), align= "center")
    
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER! final score: {self.score}", font=("Courier", 20), align= "center")