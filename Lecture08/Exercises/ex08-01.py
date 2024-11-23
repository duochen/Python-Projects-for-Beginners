# Define the initial empty board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Display the current board state
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for a win condition
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Updated function to handle the file format
def process_moves(file_path):
    board = initialize_board()

    try:
        with open(file_path, "r") as file:
            for line in file:
                move = line.strip()
                if not move:
                    continue
                try:
                    player, row, col = move.split(",")
                    player = player.strip()
                    row, col = int(row.strip()), int(col.strip())

                    if player not in {"X", "O"}:
                        print(f"Invalid player: {player}. Must be 'X' or 'O'.")
                        continue

                    if board[row][col] == " ":
                        board[row][col] = player
                        winner = check_winner(board)
                        if winner:
                            display_board(board)
                            print(f"Player {winner} wins!")
                            return
                    else:
                        print(f"Invalid move: Cell ({row}, {col}) is already occupied.")
                except (ValueError, IndexError):
                    print(f"Invalid move format or out of bounds: {move}")
        display_board(board)
        print("Game over! It's a draw." if not check_winner(board) else f"Player {check_winner(board)} wins!")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

# Test the function with an example file (you can replace this with your file path)
test_file_path = "tic_tac_toe_moves.txt"
process_moves(test_file_path)
