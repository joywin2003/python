from turtle import Turtle
import random
from turtle import Screen
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1,10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            new_car.setheading(-180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT


# screen = Screen()
# screen.setup(width=600, height=600)
# cars = CarManager()
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     cars.create_cars()
#     cars.move_car()
#
# screen.exitonclick()