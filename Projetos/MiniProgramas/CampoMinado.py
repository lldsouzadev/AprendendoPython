import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root: tk.Tk, rows: int, cols: int, mines: int):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flags = mines
        self.buttons = {}
        self.mine_positions = set()
        self.score = 0
        self.game_over = False
        self.create_widgets()
        self.place_mines()
        self.update_numbers()

    def create_widgets(self):
        #Cria os botões na interface gráfica e as telinhas de Score e Bombas Restantes.
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        # Telinhas de Score e Bombas Restantes
        self.score_label = tk.Label(frame, text=f"{self.score}", font=("Arial", 14))
        self.score_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.flags_label = tk.Label(frame, text=f"{self.flags}", font=("Arial", 14))
        self.flags_label.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Área de Mensagens
        self.message_label = tk.Label(frame, text="", font=("Arial", 12), fg="red")
        self.message_label.grid(row=1, column=0, columnspan=2, pady=5)

        # Grade de Botões
        board_frame = tk.Frame(self.root, relief=tk.SUNKEN, borderwidth=3)
        board_frame.pack(padx=10, pady=10)

        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(board_frame, width=2, height=1, command=lambda r=r, c=c: self.on_click(r, c))
                btn.bind("<Button-3>", lambda event, r=r, c=c: self.on_right_click(r, c))
                btn.grid(row=r, column=c)
                self.buttons[(r, c)] = btn

        # Botão de Reiniciar
        self.restart_button = tk.Button(self.root, text="Reiniciar", command=self.restart_game, state="disabled")
        self.restart_button.pack(pady=10)

    def place_mines(self):
        #Distribui as minas aleatoriamente no campo.
        while len(self.mine_positions) < self.mines:
            position = (random.randint(0, self.rows-1), random.randint(0, self.cols-1))
            self.mine_positions.add(position)

    def update_numbers(self):
        #Atualiza os números nos botões com base nas minas adjacentes.
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r, c in self.mine_positions:
            self.board[r][c] = -1  # Representa uma mina

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                mines_count = sum(
                    (r + dr, c + dc) in self.mine_positions
                    for dr in [-1, 0, 1]
                    for dc in [-1, 0, 1]
                    if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols
                )
                self.board[r][c] = mines_count

    def on_click(self, r: int, c: int):
        #Lida com o clique do usuário em um botão.
        if self.game_over:
            return

        if self.board[r][c] == -1:
            self.buttons[(r, c)].config(text="*", bg="red")
            self.reveal_mines()
            self.message_label.config(text="Você perdeu!")
            self.game_over = True
            self.restart_button.config(state="normal")
        else:
            self.reveal(r, c)
            self.update_score()

        if self.check_victory():
            self.message_label.config(text="Você venceu!")
            self.game_over = True
            self.restart_button.config(state="normal")

    def on_right_click(self, r: int, c: int):
        #Lida com o clique direito para marcar/desmarcar uma bandeira.
        if self.game_over:
            return

        btn = self.buttons[(r, c)]
        if btn["text"] == "":
            if self.flags > 0:
                btn.config(text="⚑", fg="red")
                self.flags -= 1
        elif btn["text"] == "⚑":
            btn.config(text="")
            self.flags += 1
        self.update_flags_label()

    def reveal(self, r: int, c: int):
    #Revela o conteúdo de uma célula e as adjacentes se for 0.
        if self.buttons[(r, c)]["text"] != "" or self.buttons[(r, c)]["state"] == "disabled":
            return

        if self.board[r][c] > 0:
            self.buttons[(r, c)].config(text=str(self.board[r][c]), state="disabled", relief=tk.SUNKEN)
        elif self.board[r][c] == 0:
            self.buttons[(r, c)].config(state="disabled", relief=tk.SUNKEN)
            # Revela todos os vizinhos se a célula atual for 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.reveal(nr, nc)

    def reveal_mines(self):
        #Revela todas as minas no campo.
        for r, c in self.mine_positions:
            self.buttons[(r, c)].config(text="*", bg="red", state="disabled")

    def update_score(self):
        #Atualiza o score com base nos cliques corretos.
        self.score += 1
        self.score_label.config(text=f"{self.score}")

    def update_flags_label(self):
        #Atualiza a tela que mostra o número de bandeiras restantes.
        self.flags_label.config(text=f"{self.flags}")

    def check_victory(self) -> bool:
        #Verifica se o jogador venceu o jogo.
        cleared_cells = sum(
            1 for r in range(self.rows) for c in range(self.cols)
            if self.board[r][c] >= 0 and self.buttons[(r, c)]["state"] == "disabled"
        )
        return cleared_cells == (self.rows * self.cols - self.mines)

    def restart_game(self):
        #Reinicia o jogo.
        self.root.destroy()
        main()

def main():
    root = tk.Tk()
    root.title("Campo Minado")
    game = Minesweeper(root, rows=10, cols=10, mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
