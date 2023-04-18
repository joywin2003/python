import turtle
from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(width=800, height=400)
user_bet = screen.textinput(title="Enter your bet", prompt="Which color turtle you wanna bet on")
# print(user_bet)
color = ["red", "green", "blue", "yellow", "purple", "grey"]
pos = -120
our_turtle = []
for turtles in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=pos)
    pos += 40
    our_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in our_turtle:
        if turtle.xcor()>380:
            winning_turtle = turtle.pencolor()
            if our_turtle == winning_turtle:
                print(f"You won the bet! {winning_turtle} reached first")
            else:
                print(f"You lost the bet! {winning_turtle} reached first")
            race_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)




# jos = Turtle(shape = "turtle")
# jos.color("blue")
# jos.penup()
# jos.goto(x= -230, y =-60)
#
# chris = Turtle(shape = "turtle")
# chris.color("green")
# chris.penup()
# chris.goto(x= -230, y =0)
#
# canon = Turtle(shape = "turtle")
# canon.color("yellow")
# canon.penup()
# canon.goto(x= -230, y =60)
#
# joshua = Turtle(shape = "turtle")
# joshua.color("black")
# joshua.penup()
# joshua.goto(x= -230, y =120)
#


screen.exitonclick()
