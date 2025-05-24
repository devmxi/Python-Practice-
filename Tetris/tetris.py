from turtle import Turtle, Screen
from tetr_I import TeterI
from tetr_O import TeterO
from gui import Gui
import random
import time

# setup screen
screen = Screen()     
screen.setup(width=800, height=1000)
screen.bgcolor("black")
screen.title("Tetris")
screen.tracer(0)

class GameState:
    def __init__(self):
        self.GRID_WIDTH = 10
        self.GRID_HEIGHT = 20
        self.CELL_SIZE = 20
        self.BOARD_LEFT = -180
        self.BOARD_RIGHT = 180
        self.BOARD_BOTTOM = -480
        self.board = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]

game_state = GameState()
gui = Gui() #set up gui 
ycor = 0
xcor = 0
I_count = 2

blocks = [lambda: TeterI(game_state), lambda: TeterO(game_state)]
current_blk = random.choice(blocks)()

screen.update()

def go_left():
    current_blk.left()
    screen.update()

def go_right():
    current_blk.right()
    screen.update()

def rotate_blk():
    if hasattr(current_blk, 'rotate'): 
        current_blk.rotate()
        screen.update()
    

screen.listen()
screen.onkey(key="Left", fun=go_left)
screen.onkey(key="Right", fun=go_right)
screen.onkey(key="z", fun=rotate_blk)

current_blk.spawn()

def add_to_board(block):
    segments = block.tetr_I_blk if hasattr(block, 'tetr_I_blk') else block.tetr_O_blk
    for segment in segments:
        grid_x = int((segment.xcor() - game_state.BOARD_LEFT) // game_state.CELL_SIZE)
        grid_y = int((segment.ycor() - game_state.BOARD_BOTTOM) // game_state.CELL_SIZE)
        if 0 <= grid_y < game_state.GRID_HEIGHT and 0 <= grid_x < game_state.GRID_WIDTH:
            game_state.board[grid_y][grid_x] = 1


def clear_lines():
    lines_cleared = 0
    new_board = []
    
    for row in game_state.board:
        if all(row):  # If all cells in the row are filled
            lines_cleared += 1
        else:
            new_board.append(row)
    
    # Add empty rows at the top for each line cleared
    for _ in range(lines_cleared):
        new_board.insert(0, [0] * game_state.GRID_WIDTH)
    
    game_state.board = new_board
    return lines_cleared

# Call this after adding a block to the board
add_to_board(current_blk)
lines = clear_lines()



game_is_on = True
while game_is_on:
    # Try to move current block
    if not current_blk.move():
        # Block can't move down anymore
        add_to_board(current_blk)
        current_blk = random.choice(blocks)()
        current_blk.spawn()
        
        if current_blk.would_collide():
            print("Game Over!")
            game_is_on = False
    
    screen.update()
    time.sleep(0.1)
    
screen.exitonclick()