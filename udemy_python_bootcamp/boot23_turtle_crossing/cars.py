from turtle import Turtle
from random import choice

class Cars(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        y_top = height - 50
        y_bottom = (height-50)*(-1)
        self.starting_pos_x = (width - 10)*(-1)
        self.end_pos_x = width-20
        self.starting_pos_y = choice( [i for i in range(y_bottom, y_top, 30)])
        self.shapesize(stretch_wid=None, stretch_len=2)
        color_choice = choice(["red", "green", "blue", "cyan", "turquoise", "skyblue", "yellow", "chocolate1"])
        self.color(color_choice) 
        self.setheading(0)
        self.shape("square")
        self.create_car()
    
    def create_car(self):
        self.hideturtle()
        self.goto(self.starting_pos_x, self.starting_pos_y)
        self.showturtle()
    
    def move(self):
        if self.xcor() <= self.end_pos_x:
            self.forward(40)
        else:
            self.create_car()

