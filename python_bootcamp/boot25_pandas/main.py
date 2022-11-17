import pandas as pd
import turtle
from states import States
from scoreboard import Scoreboard

bgpic = "/Users/G020772/workspace/python_bootcamp/boot25_pandas/blank_states_img.gif"
states = States()
scoreboard = Scoreboard()
screen = turtle.Screen()
sh = turtle.Turtle()

# Screen the size of image:
screen.addshape(bgpic)

# Turtle draws image on screen:
sh.shape(bgpic)
scoreboard.show_scores()

# Game play:
game_on = True

while game_on:
    # User input
    text = screen.textinput("States game", "Type a state").lower()
    #Check if state exist on csv
    if states.confirm_state(text):
        states.draw_state(text)
        scoreboard.score += 1
        scoreboard.show_scores()
    else:
        game_on = False
        scoreboard.final_score()

screen.exitonclick()