import turtle
from turtle_utils import TurtleUtils

obj = TurtleUtils()
timmy = obj.get_turtle_obj("red", "turtle", 2)

flag = True
for i in range(4):

    for _ in range(20):
        timmy.pen(pendown=flag)
        timmy.forward(5)
        flag = not flag
    timmy.left(90)
obj.get_screen_click()
