from turtle import Turtle

MOVEMENT_SPEED = 20

class TeterO(Turtle):
    def __init__(self, game_state):
        super().__init__()
        self.game_state = game_state  # Reference to shared game state
        self.xvalue = 0 
        self.yvalue = 0
        self.tetr_O_start_cor = [(0,430), (20, 430), (0, 410), (20, 410)]
        self.tetr_O_blk = []
        self.count = 2

        
    def spawn(self):
        for cor in self.tetr_O_start_cor:
            newturtle = Turtle("square")
            newturtle.penup()  
            newturtle.color("orange", "yellow")
            newturtle.speed("fastest")
            newturtle.goto(cor)
            newturtle.setheading(270)
            self.tetr_O_blk.append(newturtle)
        return self.tetr_O_blk
    
    def move(self):
            if not self.would_collide(dy=-MOVEMENT_SPEED):
                for seg in self.tetr_O_blk:
                    seg.forward(MOVEMENT_SPEED)
                return True
            return False
            
    def left(self):
        if not self.would_collide(dx=-20):
            for seg in self.tetr_O_blk:
                seg.goto(seg.xcor() - 20, seg.ycor())

    def right(self):
        if not self.would_collide(dx=20):
            for seg in self.tetr_O_blk:
                seg.goto(seg.xcor() + 20, seg.ycor())
            
    def would_collide(self, dx=0, dy=0):

        for segment in self.tetr_O_blk:
            new_x = segment.xcor() + dx
            new_y = segment.ycor() + dy
            
            # Check boundaries
            if new_x < self.game_state.BOARD_LEFT or new_x >= self.game_state.BOARD_RIGHT:
                return True
            if new_y <= self.game_state.BOARD_BOTTOM:
                return True
                
            # Convert to grid coordinates
            grid_x = int((new_x - self.game_state.BOARD_LEFT) // self.game_state.CELL_SIZE)
            grid_y = int((new_y - self.game_state.BOARD_BOTTOM) // self.game_state.CELL_SIZE)
            
            # Check against game board
            if 0 <= grid_y < self.game_state.GRID_HEIGHT and 0 <= grid_x < self.game_state.GRID_WIDTH:
                if self.game_state.board[grid_y][grid_x] == 1:
                    return True
                    
        return False