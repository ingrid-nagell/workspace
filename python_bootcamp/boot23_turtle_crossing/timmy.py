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
    
    def loosing(self, car_obj):
        if (self.ycor() >= (car_obj.ycor()-10)) and (self.ycor() <= (car_obj.ycor()+10)) and (self.distance(car_obj) < 20):
            return True
        else:
            pass


'''
(0.00,-290.00) (-170.00,140.00)

car 180
turtle collide {190, 170}

'''