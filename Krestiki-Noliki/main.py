import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.current_player = self.choose_first_player()
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []
        self.create_board()

    def choose_first_player(self):
        result = messagebox.askquestion("Выбор первого игрока", "Хотите начать первым?\nДа - Крестик\nНет - Нолик")
        return "X" \
            if result == "yes"\
            else "O"

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Arial", 50), width=2, height=1,
                                   command=lambda row=i, col=j: self.mark_cell(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        restart_button = tk.Button(self.master, text="Restart", command=self.reset_board)
        restart_button.grid(row=3, columnspan=3)

    def mark_cell(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            if self.check_win():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.change_player()

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def show_winner(self):
        winner = self.current_player
        messagebox.showinfo("Победитель", f"Победил - {winner}!")

    def show_draw(self):
        messagebox.showinfo("Ничья", "Ничья!")

    def reset_board(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()