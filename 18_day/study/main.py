from turtle import Turtle, Screen
from random import random

tim = Turtle()

def polygon(sides):
    angles = 360 / sides
    color_pallet = choose_color()
    tim.pencolor(color_pallet[0], color_pallet[1], color_pallet[2])
    for _ in range(sides):
        tim.forward(100)
        tim.right(angles)

def choose_color():
    color_pallet = []
    for _ in range(3):
        color = random()
        color_pallet.append(color)

    print(color_pallet)
    return color_pallet

for i in range(3,9):
    polygon(i)
    i += 1



screen = Screen()
screen.exitonclick()

