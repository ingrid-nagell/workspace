from turtle import Turtle, Screen, color
from random import randint, choice
from time import sleep
from snake import Snake
from food import Food
from frame import Canvas

# Screen options:
canvas_size = 300
canvas = Canvas(screen_size=canvas_size)
screen = canvas.create_screen()
canvas.create_frame()

# Create a snake object of initial length = 3
snake = Snake(snake_length=3, speed="slow")
print(snake.snake_length)

food = Food(screen_size=canvas_size)
print(food)
#Lager en ny turtle for hver iterasjon. Men kan vi ikke bare lage nye kordinater? :) 

foof = True
while foof:
    speed = snake.speed
    canvas.score_board(score = snake.snake_length-3, level = snake.level, speed=snake.speed)
    food.food_move()
    bite_xcor = food.food_coordinates()[0]
    bite_ycor = food.food_coordinates()[1]
    game_on = True
    while game_on:
        screen.update()
        sleep(0.1)
        snake.snake_head.forward(20)
        snake.snake_move_body()
        snake.snake_continue(screen_size=canvas_size)
        snake.keys(screen_obj = screen)
        game_on = snake.snake_eat(food_x=bite_xcor, food_y=bite_ycor)

screen.exitonclick()

# Snake speed + lvl virker ikke...