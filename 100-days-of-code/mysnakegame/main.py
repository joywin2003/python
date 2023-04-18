from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

joy = Turtle()
screen = Screen()
screen.title("My Snake Game")
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True
points = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segment[0].distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 \
    #         or snake.segment[0].ycor() < -280:
    #     game_on = False
    #     scoreboard.gameover()
    for seg in snake.segment[1:len(snake.segment)]:
            if snake.segment[0].distance(seg)<10:
                game_on = False
                scoreboard.gameover()



screen.exitonclick()
