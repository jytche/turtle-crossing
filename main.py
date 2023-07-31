import time
from turtle import Screen, Turtle
import player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = player.Player()
FINISH_LINE_Y = (0, 280)
car_list = []

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

delay = 0.2
instance_to_create = 6
counter = 0


def create_car():
    car = CarManager()
    return car


game_is_on = True
while game_is_on:
    time.sleep(delay)
    screen.update()
    counter += 1
    if counter == instance_to_create:
        new_car = create_car()

        car_list.append(new_car)
        counter = 0
    if player.distance(FINISH_LINE_Y) < 50:
        player.reset_position()
        scoreboard.increase_score()
        for car in car_list:
            car.speed_up()
    for car in car_list:
        car.move()
        if player.distance(car) < 10:
            game_is_on = False
            scoreboard.game_over()


    # Detect collision with Car







screen.exitonclick()
