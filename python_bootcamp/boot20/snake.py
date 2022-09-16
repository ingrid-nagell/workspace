from turtle import Turtle, shape
from random import randint
from time import sleep

class Snake():
	'''Creates a snake-class, with an initial turtle-object representing the snake-object.'''
	def __init__(self, snake_length=0, speed="slow"):
		self.x_cor = 0
		self.y_cor = 0
		self.snake_length = snake_length
		self.snake = []

		for i in range(0, self.snake_length):
			segment = Turtle(shape="square")
			segment.penup()
			segment.color("white")
			segment.goto(self.x_cor, self.y_cor)
			self.snake.append(segment)
			self.x_cor -= 20
		
		self.snake_head = self.snake[0]
		self.speed = speed
		self.snake_head.speed(speed)

		self.length = int(len(self.snake))
		self.level = 1
	
	def snake_move_body(self):
		'''Creates a for-loop to move the snakesegment to the position of the first segment.'''
		for segment in range(len(self.snake)-1, 0, -1):
			new_x = self.snake[segment - 1].xcor()
			new_y = self.snake[segment - 1].ycor()
			self.snake[segment].goto(new_x, new_y)

	def snake_continue(self, screen_size):
		'''Function to keep the snake moving when it hits the walls.'''
		self.space_p = screen_size
		self.space_n = screen_size
		#self.snake_head.forward(20)
		if self.snake_head.xcor() > self.space_p:
			self.snake_head.setx(-self.space_n)
		elif self.snake_head.xcor() < -self.space_n:
			self.snake_head.setx(self.space_p)
		elif self.snake_head.ycor() > self.space_p:
			self.snake_head.sety(-self.space_n)
		elif self.snake_head.ycor() < -self.space_n:
			self.snake_head.sety(self.space_p)

	# Direction-functions to use in keys-function:
	def snake_head_north(self):
		self.snake_head.setheading(90)

	def snake_head_south(self):
		self.snake_head.setheading(270)
	
	def snake_head_east(self):
		self.snake_head.setheading(0)
	
	def snake_head_west(self):
		self.snake_head.setheading(180)
	
	def keys(self, screen_obj):
		'''Function wich enables controls. Press key:
		w to move north
		s to move south
		a to move west
		d to move east'''
		screen_obj.listen()
		screen_obj.onkey(key="w", fun=self.snake_head_north)
		screen_obj.onkey(key="s", fun=self.snake_head_south)
		screen_obj.onkey(key="a", fun=self.snake_head_west)
		screen_obj.onkey(key="d", fun=self.snake_head_east)

	def snake_grow(self):
		"Appends a snake-turtle object to the snake list."
		growing = Turtle(shape="square")
		growing.penup()
		growing.color("white")
		self.snake.append(growing)
		growing.goto(self.snake[-1].xcor(), self.snake[-1].ycor())

	def snake_lvl(self):
		if self.snake_length >= 5:
			self.level = 2
			self.snake_head.speed("normal")
			self.speed = "normal"
		elif self.snake_length >= 8:
			self.level = 3
			self.snake_head.speed("fast")
			self.speed = "fast"
		elif self.snake_length >= 10:
			self.level = 4
			self.snake_head.speed("fastest")
			self.speed = "fastest"

	def snake_eat(self, food_x, food_y):
		'''Matches the snake-head to the food coordinates.'''
		if int(self.snake_head.xcor()) in food_x and int(self.snake_head.ycor()) in food_y:
			self.game_status = False
			self.snake_grow()
			self.snake_length += 1
			self.snake_lvl()
			return self.game_status
		else:
			self.game_status = True
			return self.game_status
