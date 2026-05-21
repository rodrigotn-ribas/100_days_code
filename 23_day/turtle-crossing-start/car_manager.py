from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.penup()
        self.goto(400,400)
        self.speed = 0.2


    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 5:
            cars = Turtle()
            cars.shape("square")
            cars.color(random.choice(COLORS))
            cars.penup()
            cars.shapesize(1, 2)
            cars.goto(280, random.randint(-250, 250))
            self.car_list.append(cars)

    def move(self):
        for car in self.car_list:
            car.forward(-STARTING_MOVE_DISTANCE)

    def collision(self):
        for car in self.car_list:
            print(car.pos())

    def raise_difficulty(self):
        self.speed *= 0.5
