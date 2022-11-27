import turtle
import random


def get_random_pencolor(turtle_obj):
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    tup = (r,g,b)
    print(tup)
    turtle_obj.pencolor(tup)


class TurtleUtils:

    def __init__(self):
        self.turtle_obj = turtle.Turtle()
        self.screen_obj = turtle.Screen()

    def get_turtle_obj(self, t_color, t_shape, t_speed):
        self.turtle_obj.shape(t_shape)
        self.turtle_obj.color(t_color)
        self.turtle_obj.speed(t_speed)
        return self.turtle_obj

    def get_screen_click(self):
        self.screen_obj.exitonclick()
