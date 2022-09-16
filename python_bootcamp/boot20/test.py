txt = "Hello World"

from time import sleep

from turtle import Turtle, Screen, exitonclick

screen = Screen()

food_object = Turtle(shape="square")
food_object.setposition(23, 100)

snake_object = Turtle("turtle")
snake_object.setposition(20, 99)

screen.exitonclick()


def food_element(self):
        '''Returns a turtle object representing a food object.'''
        self.food_elem = Turtle(shape = "square")
        self.food_elem.hideturtle()
        self.food_elem.penup()
        self.food_elem.color("white")