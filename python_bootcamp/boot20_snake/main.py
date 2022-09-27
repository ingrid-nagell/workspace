from turtle import Turtle, Screen, color, textinput
from random import randint, choice
from time import sleep
from snake import Snake
from food import Food
from canvas import Canvas
from scoreboard import update_high_scores, high_score_table, list_of_nicks

high_scores_file = "python_bootcamp/boot20_snake/highscores.txt"
canvas_size = 200

play_again = True
while play_again:
    # Screen options:
    canvas = Canvas(screen_size=canvas_size)
    screen = canvas.create_screen()
    canvas.create_frame()

    # Game user inputs
    nickname = textinput("The Snake Game", "Enter your nickname.")
    while nickname in list_of_nicks(high_scores_file):
        nickname = textinput("The Snake Game", "Nickname has already been used, pick another one:")

    user_version = textinput("The Snake Game", "Enter 1 to play Snake I, enter 2 to play Snake II:")
    while user_version not in ["1", "2"]:
        user_version = textinput("Enter valid input.\nThe Snake Game", "Enter 1 to play Snake I, enter 2 to play Snake II:")

    if user_version == "1":
        screen.title("Snake I")
    elif user_version == "2":
        screen.title("Snake II")

    # Create a snake object, optional: change initial length = 3, difficulty, and startspeed. (Could add these as inputs?)
    start_length = 3
    snake = Snake(snake_length=start_length)
    food = Food(screen_size=canvas_size)

    # Game structure:
    game_not_over = True
    while game_not_over:
        canvas.score_board(score = snake.snake_length-start_length,  nickname=nickname)
        snake.keys(screen_obj = screen)
        food.food_move()
        bite_xcor = food.food_coordinates()[0]
        bite_ycor = food.food_coordinates()[1]
        game_on = True
        while game_on:
            screen.update()
            snake.snake_speed()
            snake.snake_move_body()
            collide_snake = snake.snake_collide()
            collide_wall = snake.snake_walls(screen_size=canvas_size, version=user_version)
            eat = snake.snake_eat(food_x=bite_xcor, food_y=bite_ycor)
            if collide_wall or eat or collide_snake:
                game_on = False
            if collide_wall or collide_snake:
                game_not_over = False

    # Game over:
    final_score = snake.snake_length-start_length

    update_high_scores(nickname, final_score, user_version, high_scores_file)
    high_scores = high_score_table(high_scores_file)
    canvas.highscores(nickname=nickname, score=final_score, table=high_scores)

    # Play again option:
    sleep(2)
    user_play_again = textinput("Do you want to play again?", "Enter 'y' to play again or 'n' to exit the game.").lower()
    if user_play_again == "y":
        screen.clear()
    else:
        screen.bye()


#To do:
## Reset hisghscores secret option
## Fix Highscore table - display
## Add a pause-button during game play