import random

from turtle_utils import TurtleUtils
import turtle

# Step1. Choose an input from user
ip_color = turtle.textinput("Your Turtle Color","Which color do you want to bet on?")
# Step2. create 6 objects of turtle

def get_turtle_objects():
    """on call this method returns 6 turtle objects with different colors"""
    color_list = ["red", "blue", "orange", "yellow", "green", "purple"]
    co_ordinate = -280
    turtle_obj_grp = []
    for clr in color_list:
        co_ordinate += 80
        obj = TurtleUtils()
        t_obj = obj.get_turtle_obj(clr, "turtle", 2)
        t_obj.penup()
        t_obj.setposition(-250,co_ordinate )
        turtle_obj_grp.append(t_obj)
    return turtle_obj_grp


def random_pace(turtle_obj):
    pace_limt = [1,5,9,13,18]
    pace = random.choice(pace_limt)
    turtle_obj.forward(pace)

race_participants = get_turtle_objects()
race_flag = True

obj = TurtleUtils()
race_master = obj.get_turtle_obj("black","turtle",2)
race_master.penup()
race_master.setposition(300,280)
race_master.pendown()
race_master.right(90)
race_master.forward(550)

while race_flag:
    for tt in race_participants:
        random_pace(tt)
        if tt.xcor() >= 280:
            winner = tt.color()
            race_flag = False

if winner[0] == ip_color:
    print(f"your pick is {ip_color}")
    print(f"Congratulations! You win! The winner is: {winner[0]}")
else:
    print(f"your pick is {ip_color}")
    print(f"Sorry, You lose! The winner is: {winner[0]}")
screen_obj = turtle.Screen()
screen_obj.exitonclick()
# Step3. move all of them to specific co-ordinates
# Step4. create Random pacing forward with penup
# Step5. see which one reaches specific x co-ordinate