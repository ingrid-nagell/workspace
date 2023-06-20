from turtle import Turtle
from time import sleep

class Snake():
	'''Creates a snake-class, with an initial turtle-object representing the snake-object.'''
	def __init__(self, snake_length=3, snake_speed=0.2, difficulty=10):
		self.speed = snake_speed
		self.difficulty = difficulty
		self.snake_length = snake_length
		self.snake = []
		self.create_snake(snake_length)

	def create_snake(self, length):
		self.x_cor = 0
		self.y_cor = 0
		for i in range(0, length):
			segment = Turtle(shape="square")
			segment.hideturtle()
			segment.penup()
			segment.color("white")
			segment.goto(self.x_cor, self.y_cor)
			self.x_cor -= 20
			self.snake.append(segment)
			segment.showturtle()
		
		self.snake_head = self.snake[0]
	

	def snake_move_body(self):
		'''Creates a for-loop to move the snakesegment to the position of the first segment.'''
		for segment in range(len(self.snake)-1, 0, -1):			
			new_x = self.snake[segment - 1].xcor()
			new_y = self.snake[segment - 1].ycor()
			self.snake[segment].goto(new_x, new_y)
		self.snake_head.forward(20)


	def snake_walls(self, screen_size, version):
		'''Function to keep the snake moving when it hits the walls.'''
		self.space_p = screen_size
		self.space_n = screen_size
		if version == "1" and (
			(self.snake_head.xcor() > self.space_p) or (
				self.snake_head.xcor() < -self.space_n) or (
					self.snake_head.ycor() > self.space_p) or (
						self.snake_head.ycor() < -self.space_n
						)):
			return True
		elif version == "2":
			if self.snake_head.xcor() > self.space_p:
				self.snake_head.setx(-self.space_n)
			elif self.snake_head.xcor() < -self.space_n:
				self.snake_head.setx(self.space_p)
			elif self.snake_head.ycor() > self.space_p:
				self.snake_head.sety(-self.space_n)
			elif self.snake_head.ycor() < -self.space_n:
				self.snake_head.sety(self.space_p)
			return False


	def snake_collide(self):
		self.snake_coor = []
		self.snake_head_pos = (int(self.snake_head.xcor()), int(self.snake_head.ycor()))

		for segment in self.snake[1:]:
			coor = (int(segment.xcor()), int(segment.ycor()))
			self.snake_coor.append(coor)

		if self.snake_head_pos in self.snake_coor:
			return True
		else:
			return False


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
		'''Function wich enables controls. 
		Press key:
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
		growing = Turtle(shape = "turtle")
		growing.hideturtle()
		growing.penup()
		growing.color("white")
		growing.shape("square")
		growing.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
		self.snake.append(growing)
		growing.showturtle()


	def snake_speed(self):
		sleep(self.speed)


	def snake_increase_speed(self):
		if self.snake_length % self.difficulty == 0:
			increase_speed = round(self.speed/2.5, 3)
			self.speed -= round(increase_speed, 3)


	def snake_eat(self, food_x, food_y):
		'''Matches the snake-head to the food coordinates and activates snake_grow() function.'''
		# Snake_head reaches food:
		if int(self.snake_head.xcor()) in food_x and int(self.snake_head.ycor()) in food_y:
			self.snake_grow()
			self.snake_length += 1
			# Keep track of speed when eating:
			self.snake_increase_speed()
			return True
		else:
			return False