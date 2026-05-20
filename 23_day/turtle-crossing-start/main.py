import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_cars()
    car.move()

    #Detect turtle collision wall
    if turtle.ycor() > 280:
        turtle.next_level()

    #Detect turtle collision car
    if turtle.distance(car) < 0:
        game_is_on = False
