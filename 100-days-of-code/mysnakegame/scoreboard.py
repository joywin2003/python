from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scores()

    def update_scores(self):
        self.write(f"score = {self.score}", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scores()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



