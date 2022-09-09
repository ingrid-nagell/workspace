color_palette = [(248, 236, 243), (220, 105, 160), (246, 233, 230), (141, 107, 50), (165, 38, 170), (246, 57, 80), (216, 228, 231), (68, 219, 199), (241, 162, 104), (3, 45, 141), (230, 240, 236), (242, 140, 65), (2, 186, 144), (19, 127, 166), (163, 53, 57), (250, 23, 228), (163, 167, 173), (254, 0, 231), (233, 189, 165), (32, 213, 192), (245, 150, 168), (143, 225, 213), (167, 183, 207), (105, 97, 46), (4, 37, 121)]

import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
timmy.setpos(-200, -200)

for n in range(10):
    for n in range(10):
        timmy.dot(20, random.choice(color_palette)) 
        timmy.fd(50)
    timmy.backward(500)
    timmy.setheading(90)
    timmy.fd(50)
    timmy.setheading(0)

screen.exitonclick()