import turtle
from turtle_utils import TurtleUtils

obj = TurtleUtils()
tim = obj.get_turtle_obj("red", "turtle", 2)

def fxu():
    tim.forward(50)
    tim.left(90)
    tim.backward(50)


obj.screen_obj.listen()
obj.screen_obj.onkeypress(fun=fxu,key="space")

# abc = turtle.textinput("AGE","Whats your age buddy? ")
# print(abc)
obj.screen_obj.exitonclick()
