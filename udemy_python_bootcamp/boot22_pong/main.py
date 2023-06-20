from turtle import Screen, textinput, clear
from draw import Draw
from paddle import Paddle
from ball import Ball
from scoreboard import Scores
from time import sleep

screen_width = 300
screen_height = 200

play_again = True

while play_again:
    screen = Screen()
    screen.tracer(0)
    screen.screensize(canvwidth=screen_width, canvheight=screen_height, bg="black")
    screen.title("The Game of Pong")

    scores = Scores(height=screen_height, width=screen_width)
    paddle_l = Paddle(paddle_side="left", width=screen_width, height=screen_height)
    paddle_r = Paddle(paddle_side="right", width=screen_width, height=screen_height)
    ball = Ball()
    draw = Draw(width=screen_width, height=screen_height)
    draw.frame()
    draw.net()

    p1 = textinput("Who is playing Pong?", "Type in the name of player1:")
    p2 = textinput("Who is playing Pong?", "Type in the name of player2:")
    points = int(textinput("How many points do you play for?", "Enter a number:"))

    draw.titles(player1=p1, player2=p2)

    #up = textinput(f"{p1}", "Press a key to select how to navigate the padde upwards:")
    #down = textinput(f"{p1}", "Press a key to select how to navigate the padde upwards:")
    paddle_l.move(screen, up_key = "w", down_key = "s")
    paddle_r.move(screen, up_key = "Up", down_key = "Down")

    game_on = True
    while game_on:
        screen.update()
        sleep(0.08)
        ball.move()
        ball.detect_wall(screen_height)
        ball.detect_sides(screen_width, paddle_l, paddle_r, score_func=scores.scores_update, player1=p1, player2=p2)
        if scores.score_left == points or scores.score_right == points:
            game_on = False


    ball.hideturtle()
    paddle_r.hideturtle()
    paddle_l.hideturtle()

    if scores.score_left > scores.score_right:
        winner = p1
    else:
        winner = p2
    draw.game_end(winner)
    screen.update()

    play_input = textinput("Play again?", "Type 'y' to play again, press 'ok' and click anywhere to exit.")
    if play_input.lower() == 'y':
        screen.clearscreen()
    else:
        play_again=False
        screen.exitonclick()