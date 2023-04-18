from turtle import Turtle,Screen
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset()

    def reset(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    # def winner(self):
    #     if self.ycor() > FINISH_LINE_Y:
    #         Scoreboard.cross_the_line()

