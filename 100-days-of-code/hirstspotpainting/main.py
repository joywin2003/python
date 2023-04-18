# import colorgram
# import colorgram.colorgram
#
# colors = colorgram.extract('image.jpg',10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r,g,b)
#     rgb_colors.append(tuple)
# print(rgb_colors)
import turtle
import random

joy = turtle.Turtle()
turtle.colormode(255)
color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214),
              (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170)]
joy.hideturtle()
joy.penup()
joy.setheading(225)
joy.forward(300)
joy.setheading(0)
joy.speed(20)
joy.pendown()
for i in range(10):
    for j in range(10):
        joy.dot(20, random.choice(color_list))
        joy.penup()
        joy.forward(50)
        joy.pendown()
    joy.setheading(90)
    joy.penup()
    joy.forward(50)
    joy.setheading(180)
    joy.forward(500)
    joy.pendown()
    joy.setheading(0)



screen = turtle.Screen()
screen.exitonclick()
