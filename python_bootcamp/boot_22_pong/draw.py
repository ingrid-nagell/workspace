from turtle import Turtle
FONT = ("Calibri", "14", "bold")

class Draw(Turtle):
    
    def __init__(self, height, width):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.height = height
        self.width = width
    
    def titles(self, player1, player2):
        self.goto(0, self.height+10)
        self.write(f"{player1} VS {player2}", font=FONT, align="center")
    
    def frame(self):
        '''Creates a frame to vizualize the game space.'''
        # Add 10, because turtle draws in the middle of 20pxls
        frame_width = self.width + 10
        frame_height = self.height + 10
        self.setposition(-frame_width, frame_height)
        self.pendown()
        self.setheading(180)
        self.goto(-frame_width, -frame_height)
        self.setheading(90)
        self.goto(frame_width, -frame_height)
        self.setheading(0)
        self.goto(frame_width, frame_height)
        self.setheading(270)
        self.goto(-frame_width, frame_height)
        self.penup()
    
    def net(self):
        net_top = self.height + 10
        net_bottom = -self.height - 10
        self.setposition(0, net_top)
        self.setheading(270)
        for i in range(0, self.height+20, 20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(0, net_bottom)
        self.penup()
    
    def game_end(self, winner):
        self.home()
        self.color("purple")
        self.write(f"The winner is: {winner}!", align="center", font=("Calibri", "18", "bold"))
    
