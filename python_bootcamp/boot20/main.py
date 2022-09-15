from turtle import Turtle, Screen, color
from random import randint, choice
from time import sleep
from snake import Snake
from food import Food
from frame import create_frame

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.title("The Snake Game")
screen.tracer(0)
create_frame(600)
screen.listen()

snake = Snake(snake_length=3)
food = Food()

foof = True
while foof:
    bite = food.food_element()
    game_on = True
    while game_on:
        screen.update()
        sleep(0.1)
        snake.snake_head.forward(20)
        snake.snake_move_body()
        snake.snake_continue()
        snake.keys(screen_obj = screen)
        snake.snake_eat(bite)

screen.exitonclick()