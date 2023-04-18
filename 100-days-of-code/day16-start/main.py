# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(80)
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
x = PrettyTable()
'''table1 = PrettyTable()
table.add_column("HomoChutiyian", ["Risha", "Reshma", "Me"])
table.add_column("Type", ["Kirkiri Aurat", "Tormentor", "Innocent victim"])
table.add_column("Chutiya Level", ["Infinitude", "BEYOND", "0"])
table.align["Type"] = "l"
table.align["Pokemon"] = "l"
table.
print(table)'''

x.field_names = ["City name", "Area"]
x.add_row(["Adelaide", 1295])
x.add_row(["Brisbane", 5905])
x.add_row(["Darwin", 112] )
x.add_row(["Hobart", 1357])
x.add_row(["Sydney", 2058])
x.add_row(["Melbourne", 1566])
x.add_row(["Perth", 5386])
print(x)


