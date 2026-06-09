from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("You win the game", align="center", font=("Arial", 100, "bold"))