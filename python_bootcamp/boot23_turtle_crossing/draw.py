from turtle import Turtle

FONT = ("Calibri", "18", "bold")

class Draw(Turtle):
    
    def __init__(self, height, width, drawing_color="black"):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(drawing_color)
        self.height = height
        self.width = width
    
    def frame(self, text):
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
        self.goto(0, frame_height)
        self.write(text)
    
    def finish_line(self):
        self.goto((self.width+10)*(-1), 260)
        self.setheading(0)
        self.color("green")
        self.write("Finish line")
        for i in range(0, self.width+10, 20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def game_over(self, winning, coallision):
        self.home()
        if winning == True:
            self.color("green")
            self.write("You Win!", align="center", font=FONT)
        elif coallision == True:
            self.color("red")
            self.write("Game Over!", align="center", font=FONT)
    
