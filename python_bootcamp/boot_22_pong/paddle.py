from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, paddle_side, width, height):
        super().__init__()
        self.penup()
        self.height = height
        self.create_paddle(side=paddle_side, screen_width=width)
        self.speed(10)
    
    def create_paddle(self, side, screen_width):
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=4)
        if side == 'left':
            self.goto(-screen_width, 0)
        elif side == 'right':
            self.goto(screen_width, 0)
    
    def go_up(self):
        new_y = (self.ycor() + 40)
        if new_y < self.height-10:
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = (self.ycor() - 40)
        if new_y > -self.height+10:
            self.goto(self.xcor(), new_y)

    def move(self, screen_obj, up_key, down_key):
        # Ask user to choose buttons!
        self.screen = screen_obj
        self.screen.listen()
        self.screen.onkeypress(self.go_up, up_key)
        self.screen.onkeypress(self.go_down, down_key)