from turtle import Turtle
from time import sleep

FONT = ("Calibri", "10", "normal")
class Scores(Turtle):
    
    def __init__(self, height, width):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.height = height
        self.width = width
        self.score_left = 0
        self.score_right = 0
        self.print_scores(self.score_left, self.score_right)

    def print_scores(self, score_l, score_r):
        top = self.height + 10
        p1_placement = -self.width
        p2_placement = self.width
        self.setposition(p1_placement, top)
        self.write(f"Score P1: {score_l}", font=FONT)
        self.setposition(p2_placement, top)
        self.write(f"Score P2: {score_r}", font=FONT, align="right")
    
    def scores_update(self, side, player):
        if side == "left":
           self.score_right += 1
        elif side == "right":
            self.score_left += 1
        self.home()
        self.color("green")
        self.write(f"Point to {player}", align="center", font=FONT)
        sleep(1)
        self.undo()
        self.color("white")
        self.clear()
        self.print_scores(self.score_left, self.score_right)
