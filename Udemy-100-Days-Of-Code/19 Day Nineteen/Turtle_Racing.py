from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
is_race_on = False
all_turtles = []
play_again = "yes"


def turtle_setup(): 
    for turtle_index in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(-230, y_positions[turtle_index])
        all_turtles.append(new_turtle)
        
    
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing")
screen.bgcolor("black") 


user_bet = screen.textinput(title="Make your bet!", prompt="What turtle will win? Enter a color: ").lower()
bet_value = screen.textinput(title="Value your bet!", prompt="How much would you like to bet? Enter a whole number: ")

turtle_setup()
    
if user_bet:
    is_race_on = True

while play_again == "yes": 
    while is_race_on:
        
        for turtle in all_turtles:
            
            if turtle.xcor() > 230:
                is_race_on = False
                turtle_winner = turtle.pencolor()
                
                if turtle_winner == user_bet:
                    screen.textinput("result", f"You've won! The {turtle_winner} turtle is the winner!")
                    bet_value = int(bet_value) * 2
                    play_again = screen.textinput("money", f"You now have {bet_value} dollars! :) congrats! Wanna win more? Enter yes or no").lower()
                else:
                    screen.textinput("result", f"You've lost! The {turtle_winner} turtle is the winner!")
                    bet_value = int(bet_value) / 2
                    play_again = screen.textinput("money", f"You now have {bet_value} dollars! :c wanna win it back? Enter yes or no").lower()
                    
            if not is_race_on: 
                break
                
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            
    if play_again == "no":
        screen.textinput("Bye-Bye", f"You now have {bet_value} dollars! Thanks for playing!")
        turtle.bye()
    elif play_again == "yes": 
        is_race_on = True
        screen.clear()
        screen.bgcolor("black") 
        all_turtles = []
        turtle_setup()
        
screen.exitonclick()