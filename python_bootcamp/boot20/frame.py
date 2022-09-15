from turtle import Turtle

def create_frame(size):
    frame = Turtle()
    frame.penup()
    frame.color("white")
    frame.setposition(-size,size)
    frame.pendown()
    frame.setheading(180)
    frame.goto(-size,-size)
    frame.setheading(90)
    frame.goto(size,-size)
    frame.setheading(0)
    frame.goto(size,size)
    frame.setheading(270)
    frame.goto(-size,size)