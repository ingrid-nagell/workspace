from turtle import Turtle

class Timmy(Turtle):
    def __init__(self, height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        starting_pos_y = (height-10)*(-1)
        self.goto(self.xcor(), starting_pos_y)
        self.showturtle()

    def move(self):
        self.forward(20)

    def winning(self, finish_line):
        if self.ycor() >= finish_line:
            return True
        else:
            pass