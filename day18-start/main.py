# from turtle import Turtle, Screen
#
# def square(self):
#     self.forward(100)
#     self.right(90)
#     self.forward(100)
#     self.right(90)
#     self.forward(100)
#     self.right(90)
#     self.forward(100)
#     self.right(90)
#     self.forward(100)
#
# diona_the_turtle = Turtle()
# diona_the_turtle.shape("arrow")
# diona_the_turtle.color("brown")
# square(diona_the_turtle)
#
from turtle import Turtle,Screen
joywin = Turtle()
for i in range(50):
    joywin.forward(10)
    joywin.penup()
    joywin.forward(10)
    joywin.pencolor("red")
    joywin.pendown()




screen = Screen()
screen.exitonclick()