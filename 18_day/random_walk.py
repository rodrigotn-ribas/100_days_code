from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
move_set = ["right", "left"]

def random_walk(move_set):
    direction = random.choice(move_set)
    color_pallet = choose_color()
    tim.pencolor(color_pallet[0], color_pallet[1], color_pallet[2])
    if direction == "right":
        tim.right(90)
        tim.forward(50)
    else:
        tim.left(90)
        tim.forward(50)
    print(direction)

def choose_color():
    color_pallet = []
    for _ in range(3):
        color = random.random()
        color_pallet.append(color)

    print(color_pallet)
    return color_pallet

while True:
    random_walk(move_set)

screen = Screen()
screen.exitonclick()

