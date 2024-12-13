# Function to draw the Tic-Tac-Toe board
def draw_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")


# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def main():
    # Initialize the board and players
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")

    # Game loop
    for turn in range(9):
        # Draw the board
        draw_board(board)

        # Prompt for valid input
        while True:
            try:
                row = int(input(f"Player {player}, enter row (0-2): "))
                col = int(input(f"Player {player}, enter column (0-2): "))
                if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                    print("Invalid move. Try again.")
                else:
                    break  # Valid input
            except ValueError:
                print("Invalid input. Enter numbers between 0 and 2.")

        # Make the move
        board[row][col] = player

        # Check for a win after making a move
        if check_win(board, player):
            draw_board(board)
            print(f"Player {player} wins!")
            return  # Exit the game after a win

        # Switch to the other player
        player = "O" if player == "X" else "X"

    # End of the game
    draw_board(board)

    # Check for a draw
    print("It's a draw!")


if __name__ == "__main__":
    main()