# main.py

import tictactoe

def play_game():
    board = tictactoe.initialize_board()
    current_player = "X"
    
    while True:
        tictactoe.print_board(board)
        
        # Get user input for the move
        print(f"Player {current_player}'s turn")
        position = int(input("Enter the position (1-9): "))

        # Validate and make the move
        if 1 <= position <= 9:
            if tictactoe.make_move(board, position, current_player):
                if tictactoe.is_winner(board, current_player):
                    tictactoe.print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif tictactoe.is_board_full(board):
                    tictactoe.print_board(board)
                    print("It's a draw!")
                    break
                else:
                    # Switch player
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move! The position is already taken. Try again.")
        else:
            print("Invalid position! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_game()
