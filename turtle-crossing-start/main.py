import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_cars()
    cars.move_car()
    if player.ycor() > 280:
        scoreboard.cross_the_line()
        cars.increase_speed()
        player.reset()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()