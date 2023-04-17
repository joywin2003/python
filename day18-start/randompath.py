import turtle as t
import random

colors = ["yellow", "gold" ,"orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise","lightgreen", "green"]

joy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuble = (r, g, b)
    return color_tuble


joy.width(10)
joy.speed(10)
for walk in range(500):
    position = random.randint(0, 1)
    #joy.color(random.choice(colors))
    rgb_color = random_color()
    joy.color(rgb_color)
    if position == 0:
        joy.left(90)
    else:
        joy.right(90)
    joy.forward(50)




screen = Screen()
screen.exitonclick()