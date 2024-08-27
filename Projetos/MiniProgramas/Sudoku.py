import tkinter as tk
from tkinter import messagebox
import random

class Sudoku:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}
        self.notes = {}
        self.board = self.generate_board()
        self.history = []  # Para armazenar o histórico das jogadas
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        for r in range(9):
            for c in range(9):
                cell_frame = tk.Frame(frame, relief=tk.SUNKEN, borderwidth=1)
                cell_frame.grid(row=r, column=c, padx=(1, 5) if c % 3 == 2 and c != 8 else 1, pady=(1, 5) if r % 3 == 2 and r != 8 else 1)
                
                cell = tk.Entry(cell_frame, width=2, font=("Arial", 16), justify="center")  # Tamanho do campo reduzido e quadrado
                cell.grid(row=0, column=0, padx=5, pady=5)

                if self.board[r][c] != 0:
                    cell.insert(0, str(self.board[r][c]))
                    cell.config(state="disabled")
                else:
                    cell.bind("<KeyRelease>", lambda event, r=r, c=c: self.on_key_release(event, r, c))

                self.cells[(r, c)] = cell
                self.notes[(r, c)] = []

        # Botões para controle
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        solve_btn = tk.Button(btn_frame, text="Resolver", command=self.solve_board)
        solve_btn.pack(side=tk.LEFT, padx=5)

        undo_btn = tk.Button(btn_frame, text="Desfazer", command=self.undo_move)
        undo_btn.pack(side=tk.LEFT, padx=5)

        reset_btn = tk.Button(btn_frame, text="Reiniciar", command=self.reset_board)
        reset_btn.pack(side=tk.LEFT, padx=5)

    def generate_board(self):
        def fill_board(board):
            for i in range(9):
                nums = list(range(1, 10))
                for j in range(9):
                    if board[i][j] == 0:
                        random.shuffle(nums)
                        for num in nums:
                            if self.is_valid(board, i, j, num):
                                board[i][j] = num
                                if fill_board(board):
                                    return True
                                board[i][j] = 0
                        return False
            return True

        def remove_numbers(board, difficulty=40):
            count = 0
            while count < difficulty:
                r = random.randint(0, 8)
                c = random.randint(0, 8)
                while board[r][c] == 0:
                    r = random.randint(0, 8)
                    c = random.randint(0, 8)
                board[r][c] = 0
                count += 1
            return board

        board = [[0 for _ in range(9)] for _ in range(9)]
        fill_board(board)
        return remove_numbers(board)

    def is_valid(self, board, r, c, num):
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False

        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def on_key_release(self, event, r, c):
        value = event.widget.get()
        if value.isdigit() and 1 <= int(value) <= 9:
            if self.is_valid(self.board, r, c, int(value)):
                self.history.append((r, c, self.board[r][c]))  # Salva o estado anterior
                if len(self.history) > 3:  # Limita o histórico a 3 jogadas
                    self.history.pop(0)
                self.board[r][c] = int(value)
                self.check_completion()  # Verifica se o jogo foi completado
            else:
                messagebox.showwarning("Inválido", "Este número não pode ser inserido nesta posição.")
                event.widget.delete(0, tk.END)
                self.board[r][c] = 0  # Resetar a posição no tabuleiro para 0, pois o número não foi aceito
        else:
            event.widget.delete(0, tk.END)
            self.board[r][c] = 0  # Garantir que o tabuleiro também reflete a remoção do número


    def check_completion(self):
        if all(all(cell != 0 for cell in row) for row in self.board):
            messagebox.showinfo("Parabéns!", "Você completou o Sudoku!")

    def undo_move(self):
        if self.history:
            r, c, previous_value = self.history.pop()
            self.board[r][c] = previous_value
            cell = self.cells[(r, c)]
            cell.config(state="normal")
            cell.delete(0, tk.END)
            if previous_value != 0:
                cell.insert(0, str(previous_value))
                cell.config(state="disabled")

    def solve_board(self):
        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == 0:
                        for num in range(1, 10):
                            if self.is_valid(board, r, c, num):
                                board[r][c] = num
                                if solve(board):
                                    return True
                                board[r][c] = 0
                        return False
            return True

        solve(self.board)
        self.update_board()

    def reset_board(self):
        self.board = self.generate_board()
        self.history.clear()
        self.update_board()

    def update_board(self):
        for r in range(9):
            for c in range(9):
                cell = self.cells[(r, c)]
                cell.config(state="normal")
                cell.delete(0, tk.END)
                if self.board[r][c] != 0:
                    cell.insert(0, str(self.board[r][c]))
                    cell.config(state="disabled")

def main():
    root = tk.Tk()
    game = Sudoku(root)
    root.mainloop()

if __name__ == "__main__":
    main()
