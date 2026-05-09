# TODO 0 : 10 x 10 dots; 20 size and space apart 50;
# TODO 1: .teleport to move, .pos to show the position,

import turtle as t
from Movement import Movement

tim = Movement()
screen = t.Screen()
screen.colormode(255)

tim.make_paint()

screen.exitonclick()