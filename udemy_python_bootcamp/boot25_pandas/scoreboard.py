from nbformat import read
import pandas as pd
import turtle

with open("/Users/G020772/workspace/python_bootcamp/boot25_pandas/highscore.txt") as f:
    HIGHSCORE = f.read()

class Scoreboard():
    def __init__(self):
        self.score = 0
        self.highscore = HIGHSCORE
        self.draw = turtle.Turtle()
        self.draw.hideturtle()
        self.draw.penup()

    def show_scores(self):
        # improve font and alignment
        self.draw.clear()
        self.draw.goto(300, 250)
        self.draw.write(f"Score: {str(self.score)}\tHighscore: {HIGHSCORE}")
    
    def final_score(self):
        # improve font and alignment
        # Ask to paly again and reset stats
        self.draw.home()
        if self.score > int(HIGHSCORE):
            with open("/Users/G020772/workspace/python_bootcamp/boot25_pandas/highscore.txt", "w") as f:
                f.write(str(self.score))
            self.draw.write(f"GAME OVER!\nYou beat the old High Score!\nYour new high score is: {str(self.score)}.")
        else:
            self.draw.write(f"GAME OVER!\nYour score was: {str(self.score)}.\nIt was not high enough to beat the high score of: {HIGHSCORE}.")