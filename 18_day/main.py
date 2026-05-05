from turtle import Turtle, Screen

tim = Turtle()

def dashed():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

for i in range(15):
    dashed()


screen = Screen()
screen.exitonclick()

