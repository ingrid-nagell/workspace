import pandas as pd
import turtle

class States():
    def __init__(self):
        self.df = pd.read_csv("/Users/G020772/workspace/python_bootcamp/boot25_pandas/usa_states.csv", sep=",")
        self.df["state"] = self.df["state"].str.lower()

    def confirm_state(self, guess):
        if len(self.df[self.df["state"] == guess]) == 1:
            return True
        else:
            return False
    
    def state_coordinates(self, guess):
        xcor = self.df[self.df["state"] == guess].iloc[0]['x']
        ycor = self.df[self.df["state"] == guess].iloc[0]['y']
        return xcor, ycor

    def draw_state(self, guess):
        x, y = self.state_coordinates(guess)
        draw = turtle.Turtle()
        draw.hideturtle()
        draw.penup()
        draw.goto(x, y)
        draw.write(f"* {guess.capitalize()}")