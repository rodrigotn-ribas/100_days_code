from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-200, 260)
        self.penup()
        self.level = 0
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME-OVER", align="center", font=FONT)

