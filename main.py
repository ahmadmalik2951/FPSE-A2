import random

ROWS = 5
COLS = 5
MINES = 5

def create_board(rows, cols, mines):
    board = [['.' for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        mine_positions.add((r, c))

    for r, c in mine_positions:
        board[r][c] = 'M'

    return board, mine_positions

def display_board(board, reveal=False):
    print("\n  " + " ".join(str(i) for i in range(COLS)))
    for i, row in enumerate(board):
        if not reveal:
            row_display = ['.' if cell == 'M' else cell for cell in row]
        else:
            row_display = row
        print(f"{i} " + " ".join(row_display))
    print()

def main():
    board, mine_positions = create_board(ROWS, COLS, MINES)
    print("Welcome to Minefield! ⚡")
    display_board(board)

if __name__ == "__main__":
    main()
