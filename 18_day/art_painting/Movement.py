import turtle
import random
class Movement(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = -300
        self.y_pos = -300
        self.list_color = [
        (243, 243, 245),(186, 163, 24),
        (244, 241, 233), (48, 95, 140),
        (215, 154, 104), (163, 80, 44),
        (234, 242, 238), (242, 234, 239),
        (224, 209, 106), (16, 36, 59)]
        self.hideturtle()


    def inicialize(self):
        return self.teleport(self.x_pos, self.y_pos)

    def x_move(self):
        for _ in range(10):
            print(f"x = {self.x_pos}, y = {self.y_pos}")
            self.x_pos += 50
            self.teleport(self.x_pos, self.y_pos)
            self.dot(20, random.choice(self.list_color))

    def y_move(self):
        self.x_pos = -300
        self.y_pos += 50
        self.teleport(self.x_pos,self.x_pos)
        print(f"x = {self.x_pos}, y = {self.y_pos}")


    def make_paint(self):
        self.inicialize()
        for _ in range(10):
            self.x_move()
            self.y_move()

tim = Movement()

# for _ in range(10):
#     print(x_move(x,y))
#     print(y_move(x,y))