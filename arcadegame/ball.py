from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
        

