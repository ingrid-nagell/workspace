from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")


def move_fd():
    timmy.fd(20)

def move_bk():
    timmy.bk(20)

def clockwise():
    timmy.setheading(timmy.heading() + 10)

def anti_clockwise():
    timmy.setheading(timmy.heading() - 10)

def clear_screen():
    timmy.reset()
    info()

def info():
    timmy.hideturtle()
    timmy.penup()
    timmy.setpos(-350, 300)
    timmy.color('black')
    style = ('Arial', 14)
    timmy.write('w: move forward\ns: move backwards\na: move clockwise\nd: move counter-clockwise\nc: reset screen', font=style, align='left')
    timmy.home()
    timmy.showturtle()
    timmy.pendown()

info()

screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anti_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()