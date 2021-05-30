from turtle import *
from random import randint

PI = 3.14
to = Turtle()
my_screen = Screen()
to.hideturtle()
to.pensize(3)
to.speed("fastest")


def random_color():
    """Get a random color in RGB tuple format"""
    colormode(255)
    return randint(0, 255), randint(0, 255), randint(0, 255)


def draw_star(size):
    """Draw a simple star (36° interior corner angles)
    params: size - length of each side"""
    to.forward(size)
    for i in range(4):
        to.right(144)
        to.forward(size)


def get_angle(n):
    """Assuming n is in radians, then returns its corresponding angle in degrees"""
    return n % 360 if n > 360 else (n * 180) / PI


def animation(size, rounds=10):
    """Star animation"""
    for i in range(rounds):
        to.setheading(get_angle(i))  # tilt to an certain degree to the left each time
        # Draw star
        to.color(random_color())
        to.begin_fill()

        draw_star(size - (size*i)//rounds)
        to.end_fill()


animation(200)
my_screen.exitonclick()
