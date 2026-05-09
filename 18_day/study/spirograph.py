import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)
    tim.forward(5)

screen = t.Screen()
screen.exitonclick()

