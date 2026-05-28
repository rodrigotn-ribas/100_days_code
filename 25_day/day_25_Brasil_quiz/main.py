import turtle
import pandas as pd
from state import State
from clock_project import Clock  # Certifique-se de que o arquivo chama clock_project.py

screen = turtle.Screen()
screen.title("Brazil States Game")
image = "Brazil_Political_Map.png"
screen.addshape(image)
turtle.shape(image)

state_name = State()

# Inicializa o relógio passando a tela como parâmetro
clock = Clock(screen)

# Carrega o CSV gerado anteriormente
states_csv = pd.read_csv("estados.csv")

state_list = []
check_answers = 0

# Alterado para 27 para incluir todos os estados + Distrito Federal do CSV
while check_answers < 27:

    # Se o tempo acabar no meio do jogo, interrompe o loop
    if clock.game_over:
        break

    answer_state = screen.textinput(title=f"{check_answers}/27 States Correct", prompt="Qual o nome de outro estado?")

    # Se o usuário clicar em "Cancel" ou fechar a janela de input, answer_state será None
    if answer_state is None:
        break

    # Formata a resposta para Title Case (ex: "são paulo" vira "São Paulo")
    formatted_answer = answer_state.title()

    if not states_csv[states_csv.NOME == formatted_answer].empty and formatted_answer not in state_list:
        state_series = states_csv[states_csv.NOME == formatted_answer]
        state_x, state_y = state_series.x.values, state_series.y.values

        # Escreve o nome no mapa usando sua classe State
        state_name.write_name((state_x[0], state_y[0]))
        state_name.write(formatted_answer)

        # BÔNUS DE TEMPO: Adiciona 10 segundos ao relógio
        clock.add_bonus_time()

        check_answers += 1
        state_list.append(formatted_answer)

# Mantém a tela aberta após o fim do jogo
screen.mainloop()