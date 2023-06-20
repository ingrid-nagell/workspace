from turtle import Screen
from draw import Draw
from cars import Cars
from time import sleep
from timmy import Timmy

screen_width = 300
screen_height = 300
finish_line_ycor = screen_height - 40

screen = Screen()
screen.tracer(0)
screen.screensize(canvwidth=screen_width, canvheight=screen_height, bg="white")
screen.title("The Game of the Turtle's Crossing")

draw = Draw(height=screen_height, width=screen_width, drawing_color="lightgray")
draw.frame(text = "Good luck!")
draw.finish_line()

timmy = Timmy(screen_height)

screen.listen()
screen.onkey(timmy.move, "Up")

level = 20
names = ["car"]*level
cars = []

for e in names:
    e = Cars(screen_width, screen_height)
    cars.append(e)
    screen.update()
    # Move every new car 
    for car in cars: # Put this in the cars function
        car.move()
screen.update()

print(timmy.pos(), cars[0].pos())

# Move all cars, one at the time, once all cars are made:
status = "play"
game_on = True
while game_on:
    for car in cars:
        if timmy.winning(finish_line=finish_line_ycor):
            status = "winning"
            game_on = False
            break
        elif timmy.loosing(car):
            status = "lose"
            game_on = False
            break
        car.move()
        sleep(0.01)
        screen.update()

draw.game_over(status=status)

screen.exitonclick()