from turtle import Turtle

FONT = ('Arial', 80, 'normal')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score}  \t {self.r_score}", align=ALIGNMENT, font=FONT)

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()


    def left_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def check_winner(self):
        if self.r_score == 1:
            self.goto(0, 0)
            self.write("RIGHT WINS", align=ALIGNMENT, font=FONT)
            return False
        elif self.l_score == 1:
            self.goto(0, 0)
            self.write("LEFT WINS", align=ALIGNMENT, font=FONT)
            return False
        else:
            return True
