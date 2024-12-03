# tictactoe.py

def initialize_board():
    """Creates an empty 3x3 Tic-Tac-Toe board numbered 1-9."""
    return [str(i) for i in range(1, 10)]

def print_board(board):
    """Displays the Tic-Tac-Toe board with positions 1 to 9."""
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)

def is_winner(board, player):
    """Checks if the given player has won."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def is_board_full(board):
    """Checks if the board is full (no empty spaces)."""
    return all(cell in ["X", "O"] for cell in board)

def make_move(board, position, player):
    """Makes a move for the given player at the specified position (1-9)."""
    if board[position - 1] not in ["X", "O"]:  # Check if the cell is not taken
        board[position - 1] = player
        return True
    else:
        return False
