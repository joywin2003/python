from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segment = []
        for pos in STARTING_POSITION:
            self.add_segment(pos)
    def add_segment(self,pos):
        tail = Turtle(shape="square")
        tail.penup()
        tail.color("white")
        tail.goto(pos)
        self.segment.append(tail)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x_pos = self.segment[seg - 1].xcor()
            y_pos = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_pos, y_pos)
        self.segment[0].forward(MOVE_FORWARD)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def extend(self):
        self.add_segment(self.segment[-1].position())

