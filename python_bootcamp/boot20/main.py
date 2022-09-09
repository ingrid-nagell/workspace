from turtle import Turtle, Screen
from random import randint
from time import sleep
from snake import Snake, snake_move

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    
	snake__move()
    snake[0].forward(20)
    snake[0].right(90)

screen.exitonclick()