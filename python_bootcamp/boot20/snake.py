from turtle import Turtle, Screen
from random import randint
from time import sleep

class Snake():
	def __init__:
		xcor = 0
		ycor = 0
		snake = []

		for i in range(0,3):
			segment = Turtle(shape="square")
			segment.penup()
			segment.color("white")
			segment.goto(xcor, ycor)
			xcor -= 20
			snake.append(segment)

	def snake_move():
		# For loop to move the snakesegment to the position of segment-1
        for segment in range(len(snake)-1, 0, -1):
			new_x = snake[segment - 1].xcor()
			new_y = snake[segment - 1].ycor()
			snake[segment].goto(new_x, new_y)
