# importing libraries to use its functions
import turtle
import random


# returns a random rgb color number
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# Creating my object "joy"
joy = turtle.Turtle()
turtle.colormode(255)
# change the speed as you desire
joy.speed(10)
joy.pensize(2)
# change the size of gap to increase or decrease gap between circles
size_of_gap = 10
# Repeatedly creating the circles but at an particular shift
for i in range(int(360/size_of_gap)):
    joy.color(random_color())
    joy.circle(100)
    joy.left(size_of_gap)
