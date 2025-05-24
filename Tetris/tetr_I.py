from turtle import Turtle

MOVEMENT_SPEED = 20

class TeterI(Turtle):
    def __init__(self, game_state):
        super().__init__()
        self.game_state = game_state  # Reference to shared game state
        self.xvalue = 0 
        self.yvalue = 0
        self.tetr_I_start_cor = [(0,430), (0, 410), (0, 390), (0, 370)]
        self.tetr_I_blk = []
        self.count = 2

        
    def spawn(self):
        for cor in self.tetr_I_start_cor:
            newturtle = Turtle("square")
            newturtle.penup()  
            newturtle.color("blue", "cyan")
            newturtle.speed("fastest")
            newturtle.goto(cor)
            newturtle.setheading(270)
            self.tetr_I_blk.append(newturtle)
        return self.tetr_I_blk
        
        
    def move(self):
        if not self.would_collide(dy=-MOVEMENT_SPEED):
            for seg in self.tetr_I_blk:
                seg.forward(MOVEMENT_SPEED)
            return True
        return False
        
    def left(self):
        if not self.would_collide(dx=-20):
            for seg in self.tetr_I_blk:
                seg.goto(seg.xcor() - 20, seg.ycor())

    def right(self):
        if not self.would_collide(dx=20):
            for seg in self.tetr_I_blk:
                seg.goto(seg.xcor() + 20, seg.ycor())
                
    def rotate(self):
        old_positions = [(seg.xcor(), seg.ycor()) for seg in self.tetr_I_blk]
        
        if self.count % 2 == 0: 
            self.yvalue = self.tetr_I_blk[2].ycor()
            self.xvalue = self.tetr_I_blk[2].xcor()
            self.tetr_I_blk[-1].goto(self.xvalue -20, self.yvalue)
            self.tetr_I_blk[0].goto(self.xvalue + 40, self.yvalue)
            self.tetr_I_blk[1].goto(self.xvalue + 20, self.yvalue)
            self.count += 1
        else: 
            self.yvalue = self.tetr_I_blk[2].ycor()
            self.xvalue = self.tetr_I_blk[2].xcor()
            self.tetr_I_blk[-1].goto(self.xvalue, self.yvalue -20)
            self.tetr_I_blk[0].goto(self.xvalue, self.yvalue + 40)
            self.tetr_I_blk[1].goto(self.xvalue, self.yvalue + 20)
            self.count += 1
        
        if self.would_collide():
            for seg, pos in zip(self.tetr_I_blk, old_positions):
                seg.goto(pos[0], pos[1])
            self.count -= 1 
    
   
    def would_collide(self, dx=0, dy=0):
        for segment in self.tetr_I_blk:
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
