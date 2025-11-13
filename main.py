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

def count_adjacent_mines(board, r, c):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'M':
            count += 1
    return count

def play_game():
    board, mine_positions = create_board(ROWS, COLS, MINES)
    revealed = set()
    safe_cells = ROWS * COLS - MINES

    print("Welcome to Minefield! ⚡")
    display_board(board)

    while True:
        try:
            r = int(input("Enter row: "))
            c = int(input("Enter column: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if (r, c) in mine_positions:
            print("💥 Boom! You hit a mine!")
            display_board(board, reveal=True)
            return

        if (r, c) in revealed:
            print("Already revealed!")
            continue

        revealed.add((r, c))
        adjacent = count_adjacent_mines(board, r, c)
        board[r][c] = str(adjacent)

        if len(revealed) == safe_cells:
            print("🎉 Congratulations! You cleared the minefield!")
            display_board(board, reveal=True)
            return

        display_board(board)

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing Minefield! 🧨")
            break

if __name__ == "__main__":
    main()
