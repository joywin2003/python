from turtle import Turtle,Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def cross_the_line(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)
