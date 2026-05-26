import turtle
import pandas as pd
from state import State



screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = State()

states_csv = pd.read_csv("50_states.csv")


state_list = []
check_answers = 0


while True:
    answer_state = screen.textinput(title=f"{check_answers}/50 States Corrects", prompt="What´s another state´s name?")
    if not states_csv[states_csv.state == answer_state.title()].empty and answer_state not in state_list:
        state_series = states_csv[states_csv.state == answer_state.title()]
        state_x, state_y = state_series.x.values, state_series.y.values
        state_name.write_name((state_x[0],state_y[0]))
        state_name.write(answer_state)
        check_answers += 1
        print(answer_state)
        state_list.append(answer_state)
    print(state_list)

screen.exitonclick()