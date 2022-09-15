from random import choice
from turtle import Turtle

class Food():
    def __init__(self):
        self.coordinate_selection = []
        for n in range(-580, 581, 20):
            self.coordinate_selection.append(n)


    def food_element(self):
        self.food_elem = Turtle(shape = "square")
        self.food_elem.penup()
        self.food_elem.color("white")
        self.food_elem.goto(choice(self.coordinate_selection), choice(self.coordinate_selection))
        return self.food_elem
