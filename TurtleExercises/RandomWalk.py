import random

import turtle_utils

obj = turtle_utils.TurtleUtils()
tim = obj.get_turtle_obj("red", "turtle", 2)

def get_random_direction():
    directions = ["left", "right"]
    return random.choice(directions)

def random_turtle_walk():
    tim.pensize(5)
    is_on = True
    score = 0
    while is_on:
        print(score)
        score += 1
        go = get_random_direction()
        turtle_utils.get_random_pencolor(tim)
        if go == "left":
            tim.left(90)
            tim.forward(20)
        elif go == "right":
            tim.right(90)
            tim.forward(20)
        if score == 80:
            is_on = False



for i in range(1,100):
    print(i)
    turtle_utils.get_random_pencolor(tim)
    tim.circle(50)
    tim.left(10)


obj.get_screen_click()