from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(350, 0)
        self.shapesize(5, 1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(350,new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(350, new_y)
