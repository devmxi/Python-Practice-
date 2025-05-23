from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen() 
play_again = "yes"

def retry():
    answer = screen.textinput(title="Retry?", prompt="Wanna play again?: Enter yes or no").lower()
    return answer

while play_again == "yes":
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detecting collision with food 
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.score +=1
            scoreboard.update()
            
        #detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.gameover()
            play_again = retry()
            
        #detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.gameover()
                play_again = retry()
        
    if play_again == "yes":
         screen.clear()
    else:
        screen.bye()

    
screen.exitonclick()

