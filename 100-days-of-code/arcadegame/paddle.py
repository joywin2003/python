from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")

    #
    def go_up(self):
        if self.ycor() < 240:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)

    def go_down(self):
        if self.ycor() > -240:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)
