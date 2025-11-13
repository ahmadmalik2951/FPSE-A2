import tkinter as tk

ROWS = 5
COLS = 5

class MinefieldGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minefield ⚡")
        self.create_grid()

    def create_grid(self):
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

    def on_click(self, r, c):
        self.buttons[r][c].config(text="Clicked", state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = MinefieldGUI(root)
    root.mainloop()
