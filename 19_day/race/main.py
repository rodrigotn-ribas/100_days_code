from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x=-230 , y=-100)
screen.exitonclick()

g = Turtle

x = -250
y = -100

for i in range(6):

    tim.goto(x=-x , y=-y)
    y += 50
