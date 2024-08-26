import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Sudoku:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}
        self.notes = {}
        self.board = self.generate_board()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        for r in range(9):
            for c in range(9):
                cell_frame = tk.Frame(frame, relief=tk.SUNKEN, borderwidth=1)
                cell_frame.grid(row=r, column=c, padx=1, pady=1)
                cell = tk.Entry(cell_frame, width=5, font=("Arial", 16), justify="center")
                cell.grid(row=0, column=0, padx=5, pady=5)

                if self.board[r][c] != 0:
                    cell.insert(0, str(self.board[r][c]))
                    cell.config(state="disabled")
                else:
                    cell.bind("<Button-1>", lambda event, r=r, c=c: self.on_click(r, c))

                self.cells[(r, c)] = cell
                self.notes[(r, c)] = []

        # Botões para controle
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        solve_btn = tk.Button(btn_frame, text="Resolver", command=self.solve_board)
        solve_btn.pack(side=tk.LEFT, padx=5)

        reset_btn = tk.Button(btn_frame, text="Reiniciar", command=self.reset_board)
        reset_btn.pack(side=tk.LEFT, padx=5)

    def generate_board(self):
        # Gera um tabuleiro de Sudoku completo e, em seguida, remove alguns números para criar um jogo.
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
            # Remove números do tabuleiro, deixando um número de pistas correspondentes à dificuldade.
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
        """Verifica se um número pode ser inserido em uma célula do Sudoku."""
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False

        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def on_click(self, r, c):
        """Lida com a inserção de números ou notas em uma célula."""
        current_value = self.cells[(r, c)].get()
        new_value = self.simple_input(f"Insira o valor para a célula ({r+1},{c+1}):")
        if new_value and new_value.isdigit() and 1 <= int(new_value) <= 9:
            if self.is_valid(self.board, r, c, int(new_value)):
                self.cells[(r, c)].delete(0, tk.END)
                self.cells[(r, c)].insert(0, new_value)
                self.board[r][c] = int(new_value)
            else:
                messagebox.showwarning("Inválido", "Este número não pode ser inserido nesta posição.")
        elif new_value and new_value.isdigit() and 0 <= int(new_value) <= 9:
            self.notes[(r, c)].append(new_value)
            note_str = ','.join(self.notes[(r, c)])
            self.cells[(r, c)].delete(0, tk.END)
            self.cells[(r, c)].insert(0, note_str)

    def simple_input(self, prompt):
        """Abre uma janela de diálogo simples para entrada do usuário."""
        return simpledialog.askstring("Input", prompt)

    def solve_board(self):
        """Resolve o tabuleiro de Sudoku (modo automático)."""
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
        """Reinicia o tabuleiro de Sudoku."""
        self.board = self.generate_board()
        self.update_board()

    def update_board(self):
        """Atualiza a interface gráfica de acordo com o estado do tabuleiro."""
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    self.cells[(r, c)].delete(0, tk.END)
                    self.cells[(r, c)].insert(0, str(self.board[r][c]))
                    self.cells[(r, c)].config(state="disabled")
                else:
                    self.cells[(r, c)].config(state="normal")
                    self.cells[(r, c)].delete(0, tk.END)

def main():
    root = tk.Tk()
    game = Sudoku(root)
    root.mainloop()

if __name__ == "__main__":
    main()
