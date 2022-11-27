import turtle_utils

FULL_DEGREES = 360

obj = turtle_utils.TurtleUtils()
tim = obj.get_turtle_obj("black", "turtle", 1)

for i in range(3, 10):
    turtle_utils.get_random_pencolor(tim)
    for m in range(i):
        tim.forward(100)
        tim.right(FULL_DEGREES/i)

obj.get_screen_click()
# for each
# Random colors
# Random angle
