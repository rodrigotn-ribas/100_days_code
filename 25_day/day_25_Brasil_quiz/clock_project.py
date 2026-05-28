import turtle


class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.time_left = 300  # 5 minutos em segundos (5 * 60)
        self.max_time = 300  # Tempo máximo permitido (5 minutos)
        self.game_over = False

        # Cria a tartaruga que vai desenhar o timer na tela
        self.timer_turtle = turtle.Turtle()
        self.timer_turtle.hideturtle()
        self.timer_turtle.penup()
        # Posiciona o timer no topo da tela (ajuste os valores se necessário)
        self.timer_turtle.goto(260, 260)

        # Inicializa o desenho do timer e começa a contagem regressiva
        self.update_display()
        self.countdown()

    def update_display(self):
        """Atualiza o texto do timer na tela."""
        self.timer_turtle.clear()

        # Converte segundos em formato MM:SS
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_string = f"Tempo: {minutes:02d}:{seconds:02d}"

        if self.game_over:
            time_string = "FIM DE JOGO! O Tempo acabou."
            self.timer_turtle.write(time_string, align="center", font=("Arial", 20, "bold"))
        else:
            self.timer_turtle.write(time_string, align="center", font=("Arial", 16, "normal"))

    def countdown(self):
        """Método assíncrono que reduz o tempo a cada 1 segundo (1000ms)."""
        if self.time_left > 0 and not self.game_over:
            self.time_left -= 1
            self.update_display()
            # Chama a si mesmo novamente após 1000 milissegundos (1 segundo)
            self.screen.ontimer(self.countdown, 1000)
        elif self.time_left <= 0:
            self.game_over = True
            self.update_display()

    def add_bonus_time(self):
        """Adiciona 10 segundos de bônus, respeitando o limite máximo de 5 minutos."""
        if not self.game_over:
            self.time_left += 10
            if self.time_left > self.max_time:
                self.time_left = self.max_time
            self.update_display()