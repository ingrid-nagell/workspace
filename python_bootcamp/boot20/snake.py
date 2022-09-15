from turtle import Turtle
from random import randint
from time import sleep

class Snake():
	def __init__(self, snake_length=0):
		self.xcor = 0
		self.ycor = 0
		self.snake_length = snake_length
		self.snake = []

		for i in range(0, self.snake_length):
			segment = Turtle(shape="square")
			segment.penup()
			segment.color("white")
			segment.goto(self.xcor, self.ycor)
			self.xcor -= 20
			self.snake.append(segment)
		
		self.snake_head = self.snake[0]
	
	def snake_move_body(self):
		# For loop to move the snakesegment to the position of segment-1
		for segment in range(len(self.snake)-1, 0, -1):
			new_x = self.snake[segment - 1].xcor()
			new_y = self.snake[segment - 1].ycor()
			self.snake[segment].goto(new_x, new_y)

	def snake_continue(self):
		#self.snake_head.forward(20)
		if self.snake_head.xcor() > 590:
			self.snake_head.setx(-590)
		elif self.snake_head.xcor() < -590:
			self.snake_head.setx(590)
		elif self.snake_head.ycor() > 590:
			self.snake_head.sety(-590)
		elif self.snake_head.ycor() < -590:
			self.snake_head.sety(590)
	
	def snake_head_north(self):
		self.snake_head.setheading(90)

	def snake_head_south(self):
		self.snake_head.setheading(270)
	
	def snake_head_east(self):
		self.snake_head.setheading(0)
	
	def snake_head_west(self):
		self.snake_head.setheading(180)

	def keys(self, screen_obj):
		screen_obj.listen()
		screen_obj.onkey(key="w", fun=self.snake_head_north)
		screen_obj.onkey(key="s", fun=self.snake_head_south)
		screen_obj.onkey(key="a", fun=self.snake_head_west)
		screen_obj.onkey(key="d", fun=self.snake_head_east)
	
	def snake_eat(self, food_object):
		if self.snake_head.position() == food_object.position():
			game_on = False
		if snake_object.xcor() in food_x and snake_object.ycor() in food_y: