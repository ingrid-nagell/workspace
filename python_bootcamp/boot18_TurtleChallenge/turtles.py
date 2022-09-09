from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
timmy = Turtle()

timmy.shape("turtle")
timmy.speed("fastest")
screen.colormode(255)
screen.colormode()

def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    random_color = (r, b, g)
    return random_color

# Dotted line:
#for i in range(15):
#    timmy.forward(10)
#    timmy.up()
#    timmy.forward(10)
#    timmy.down()

# Drawing shapes in random colors:
#for i in range(3, 11):
#    timmy.pencolor(randint(0, 255),randint(0, 255),randint(0, 255))
#    for n in range(i):
#        timmy.forward(100)
#        timmy.right(360/i)

# Drawing a random walk:
#direction = [0, 90, 180, 270]

#timmy.pensize(10)
#for i in range(100):
#    timmy.pencolor(random_color())
#    timmy.setheading(choice(direction))
#    timmy.forward(20)
# Draw a Spirograph

same_heading = True

while same_heading:
    timmy.pencolor(random_color())
    timmy.circle(100.0)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 5)
    if timmy.heading() == 0.0:
        same_heading = False

screen.exitonclick()