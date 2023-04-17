from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Arcade Game")
screen.tracer(0)
ball = Ball()
scoreboard = ScoreBoard()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
game_on = True
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.left_score()
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard.right_score()
        ball.reset()
    game_on = scoreboard.check_winner()

screen.exitonclick()
