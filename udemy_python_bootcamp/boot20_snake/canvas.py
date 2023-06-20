from turtle import Turtle, Screen

class Canvas():
    '''Creates the canvas for the Snake game.
    Change the size of the canvas by editing the screen_size parameter.
    Default size is 400 pixels.'''
    def __init__(self, screen_size = 400):
        self.drawing_timmy = Turtle()
        self.drawing_timmy.hideturtle()
        self.drawing_timmy.penup()
        self.drawing_timmy.color("white")
        self.screen_size = screen_size
        self.writing_timmy = Turtle()
        self.writing_timmy.hideturtle()
        self.writing_timmy.penup()
        self.writing_timmy.color("white")

    def create_screen(self):
        self.screen = Screen()
        self.screen.screensize(canvwidth=self.screen_size, canvheight=self.screen_size, bg="black")
        self.screen.title("The Snake Game")
        self.screen.tracer(0)
        return self.screen

    def create_frame(self):
        '''Creates a frame to vizualize the space in which the snkae moves.'''
        self.screen_size = self.screen_size + 10
        self.drawing_timmy.setposition(-self.screen_size, self.screen_size)
        self.drawing_timmy.pendown()
        self.drawing_timmy.setheading(180)
        self.drawing_timmy.goto(-self.screen_size, -self.screen_size)
        self.drawing_timmy.setheading(90)
        self.drawing_timmy.goto(self.screen_size, -self.screen_size)
        self.drawing_timmy.setheading(0)
        self.drawing_timmy.goto(self.screen_size, self.screen_size)
        self.drawing_timmy.setheading(270)
        self.drawing_timmy.goto(-self.screen_size, self.screen_size)
        self.drawing_timmy.penup()

    def score_board(self, nickname, score):
        '''Adds a score overview at the top left corner during game play.'''
        self.writing_timmy.clear()
        self.writing_timmy.setposition(-self.screen_size, self.screen_size)
        self.writing_timmy.pendown()
        self.writing_timmy.write(f"Playing as {nickname}\nScore: {score}")
        self.writing_timmy.penup()

    def highscores(self, nickname, score, table):
        '''Print users final scores and current high scores.'''
        self.screen.clear()
        self.screen.screensize(canvwidth=self.screen_size, canvheight=self.screen_size, bg="black")
        self.writing_timmy.color("white")
        self.writing_timmy.penup()
        self.writing_timmy.goto(-200,-200)
        self.writing_timmy.write(f"Game over!\n\n{nickname}, your score was {score}.\n\n" + table, font=['Verdana', 14, 'normal'])