from turtle import Turtle, Screen
from random import randint

game_on = False
screen = Screen()
screen.bgcolor("lightpink")
screen.setup(height=400, width=500)

color_list = ["red", "blue", "yellow", "green", "orange", "purple"]
y_start_pos = 150
list_of_turtles = []

prof = Turtle()
prof.hideturtle()
prof.penup()
prof.color('black')
prof.goto(x=-200, y = 50)
style = ('Arial', 16, "bold")

for col in color_list:
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x=-240, y = y_start_pos)
    new_turtle.color(col)
    new_turtle.showturtle()
    y_start_pos -= 50
    list_of_turtles.append(new_turtle)

user_bet = screen.textinput("Welcome to the races!", "Type the color of the turtle to bet on:")

if user_bet:
    game_on = True

while game_on:

    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                prof.write("You win!", font=style, align="left")
            else:
                prof.write(f"You lost!\nThe winner was the {winning_color} turtle", font=style, align="left")
            game_on = False
        else:
            turtle.forward(randint(0,10))
    

screen.exitonclick()