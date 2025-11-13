import tkinter as tk
from tkinter import messagebox
import random

ROWS = 5
COLS = 5
MINES = 5

class MinefieldGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minefield ⚡")
        self.start_game()

    def start_game(self):
        self.board = [['.' for _ in range(COLS)] for _ in range(ROWS)]
        self.mines = set()
        self.revealed = set()
        self.safe_cells = ROWS * COLS - MINES

        while len(self.mines) < MINES:
            r = random.randint(0, ROWS - 1)
            c = random.randint(0, COLS - 1)
            self.mines.add((r, c))
        for r, c in self.mines:
            self.board[r][c] = 'M'

        self.create_grid()

    def create_grid(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.buttons = []
        for r in range(ROWS):
            row_buttons = []
            for c in range(COLS):
                btn = tk.Button(
                    self.root, text=" ", width=4, height=2,
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                btn.grid(row=r, column=c, padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def count_adjacent_mines(self, r, c):
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and self.board[nr][nc] == 'M':
                count += 1
        return count

    def on_click(self, r, c):
        if (r, c) in self.mines:
            self.reveal_mines()
            messagebox.showerror("Game Over", "💥 You hit a mine! Game over!")
            self.ask_restart()
        elif (r, c) not in self.revealed:
            self.revealed.add((r, c))
            count = self.count_adjacent_mines(r, c)
            self.buttons[r][c].config(text=str(count), state="disabled", bg="lightgrey")

            if len(self.revealed) == self.safe_cells:
                self.reveal_mines()
                messagebox.showinfo("You Win!", "🎉 Congratulations! You cleared the minefield!")
                self.ask_restart()

    def reveal_mines(self):
        for (r, c) in self.mines:
            self.buttons[r][c].config(text="💣", bg="red", state="disabled")

    def ask_restart(self):
        answer = messagebox.askyesno("Restart?", "Do you want to play again?")
        if answer:
            self.start_game()
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MinefieldGUI(root)
    root.mainloop()
