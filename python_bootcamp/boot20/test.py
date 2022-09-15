txt = "Hello World"

from time import sleep

from turtle import Turtle, Screen, exitonclick

screen = Screen()

food_object = Turtle(shape="square")
food_object.setposition(23, 100)

snake_object = Turtle("turtle")
snake_object.setposition(20, 99)

food_x = []
food_y = []

for n in range(food_object.xcor()-10, food_object.xcor()+11):
	food_x.append(n)
for n in range(food_object.ycor()-10, food_object.ycor()+11):
	food_y.append(n)

print(food_x,'\n',food_y)

sleep(3)

if snake_object.xcor() in food_x and snake_object.ycor() in food_y:
	food_object.reset()

print(snake_object.xcor())

screen.exitonclick()