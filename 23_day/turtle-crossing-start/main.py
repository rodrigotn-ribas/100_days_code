import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car.speed)
    screen.update()

    #Generate cars
    car.generate_cars()
    car.move()

    #Detect turtle collision wall
    if turtle.ycor() > 280:
        turtle.next_level()
        car.raise_difficulty()
        scoreboard.level_up()

    #Detect turtle collision car
    for cars in car.car_list:
        if turtle.distance(cars.pos()) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()