from turtle import Screen, Turtle
from Paddle import Paddle

screen = Screen()
paddle = Paddle()


screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong")


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")



screen.exitonclick()