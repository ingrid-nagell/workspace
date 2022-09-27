from random import choice
from turtle import Turtle

class Food():
    '''Creates food objects for the Snake game.'''
    def __init__(self, screen_size):
        self.coordinate_selection = []
        for n in range(-(screen_size-20), (screen_size-20), 20):
            self.coordinate_selection.append(n)
        self.food_elem = Turtle()
        self.food_elem.hideturtle()
        self.food_elem.penup()
        self.food_elem.color("white")
        self.food_elem.shape("square")
    
    def food_move(self):
        '''Moves a food object to random coordinates.'''
        self.food_elem.hideturtle()
        self.food_elem.setposition(choice(self.coordinate_selection), choice(self.coordinate_selection))
        self.food_elem.showturtle()

    def food_coordinates(self):
        '''Returns two lists of integers, x-coordinates and y-coordinates for the snake to match.'''
        self.food_x = []
        self.food_y = []
        for n in range(self.food_elem.xcor()-20, self.food_elem.xcor()+21):
            self.food_x.append(n)
        for n in range(self.food_elem.ycor()-20, self.food_elem.ycor()+21):
            self.food_y.append(n)
        return self.food_x, self.food_y
