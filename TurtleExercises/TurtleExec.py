import turtle_utils

obj = turtle_utils.TurtleUtils()
tim = obj.get_turtle_obj("red", "turtle", 0)

#dash
#circle
#next line
x = -140.0
y = -140.0
for i in range(12):
    y += 30
    tim.penup()
    tim.goto(x, y)
    for _ in range(14):
        turtle_utils.get_random_pencolor(tim)
        tim.pendown()
        tim.pensize(10)
        tim.circle(5)
        tim.penup()
        tim.forward(30)

obj.get_screen_click()