from turtle import Turtle
from random import choice

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.8)
        self.direction()

    # Change to opposite serve
    def new_ball(self, side):
        self.hideturtle()
        self.home()
        self.showturtle()
        if side == 'right':
            random_int = choice([i for i in range(10, 80)] + [i for i in range(280, 350)])
            self.setheading(random_int)
        elif side == 'left':
            random_int = choice([i for i in range(100, 170)] + [i for i in range(190, 260)])
            self.setheading(random_int)

    
    #Move the ball all the time
    def move(self):
        self.forward(20)

    #Change direction
    def direction(self):
        #exclude = [0, 90, 180, 270, 360]
        random_int = choice([i for i in range(10, 80)] + [i for i in range(280, 350)] + [i for i in range(100, 170)] + [i for i in range(190, 260)])
        self.setheading(random_int)
    
    def detect_wall(self, wall_height):
        bottom_wall = - wall_height
        if self.distance(x = self.xcor(), y = wall_height)  < 10 or self.distance(x = self.xcor(), y = bottom_wall)  < 10:
            angle = self.heading()*(-1)
            self.setheading(angle)

    def detect_sides(self, wall_width, paddle_l, paddle_r, score_func, player1, player2): 
        left_wall_lim = (- wall_width) + 20
        right_wall_lim = wall_width - 20
        if (self.xcor() < left_wall_lim or self.xcor() > right_wall_lim):
            if (self.distance(paddle_l) < 50 or self.distance(paddle_r) < 50):
                angle = 180-self.heading()
                self.setheading(angle)
            else:
                if self.xcor() > 0:
                    side = "right"
                    self.player = player1
                elif self.xcor() < 0:
                    side = "left"
                    self.player = player2
                score_func(side=side, player=self.player)
                self.new_ball(side=side)