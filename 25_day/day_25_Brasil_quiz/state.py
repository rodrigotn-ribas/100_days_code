import turtle

class State(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_name(self,tuple_x_y):
        self.goto(tuple_x_y)