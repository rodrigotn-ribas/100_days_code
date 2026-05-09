# TODO 0 : 10 x 10 dots; 20 size and space apart 50;
# TODO 1: .teleport to move, .pos to show the position,

import turtle as t

# def x_move(x_movement):

# def y_move(y_movement)


tim = t.Turtle()
y = -300
x = -300
tim.teleport(x,y)

for _ in range(10):
    tim.dot(20)
    tim.teleport(x,y)
    x+=50
y+=50


screen = t.Screen()
screen.exitonclick()