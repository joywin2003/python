from turtle import Turtle, Screen

joywin = Turtle()
sides = 3
index = 0
colors = ["yellow", "gold" ,"orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise","lightgreen", "green"]
for i in range(6):
    angle = 360 / sides
    for side in range(sides):
        joywin.color(colors[index])
        joywin.forward(100)
        joywin.right(angle)
    index += 1
    sides += 1


screen = Screen()
screen.exitonclick()
