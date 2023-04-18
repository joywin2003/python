# class Employee:
#     @staticmethod
#     def greet():
#         print("Good Morning")
#
# joywin = Employee()
# joywin.greet()

class Programmer:
    company = "microsoft"

    @staticmethod
    def greet():
        print("Hello")

    def programmer_details(joy):
        joy.greet()
        joy.name = input("Enter your name")
        joy.id = input("Enter your ID")

prgm = Programmer()
prgm.programmer_details()

# class Calculator:
#     def __init__(self, number):
#         self.number = number
#
#     def square(self):
#         self.square = 1
#         for num in range(2):
#             self.square *= self.number
#         print(self.square)
#
#     def cube(self):
#         self.cube = 1
#         for num in range(3):
#             self.cube *= self.number
#         print(self.cube)
#
#     def squareRoot(self):
#         self.number **= 0.5
#         print(self.number)

class Class:
    a = 0

section1 = Class()
Class.a = 15
print(section1.a)
print(Class.a)