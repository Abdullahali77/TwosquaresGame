# Program: Two squares game. This game is played on a board of 4 x 4 squares. Two players take turns;
# each of them takes turn to place a rectangle (that covers two squares) on the board, covering
# any 2 squares. Only one rectangle can be on a square. A square cannot be covered twice. The
# last player who can place a card on the board is the winner.
# Author: Abdullah Ali Kamal
# Version: 2.0
# Date: 28/2/2023

def can_play(board):
    # Check if there are any available moves left on the board.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if col < len(board[0]) - 1:
                if board[row][col] != 'x' and board[row][col + 1] != 'x':
                    return True
            if row < len(board) - 1:
                if board[row][col] != 'x' and board[row + 1][col] != 'x':
                    return True
    return False


def is_rectangle(move1, move2):
    # Check if the selected squares form a valid rectangle

    # Convert moves to integers
    move1 = int(move1)
    move2 = int(move2)

    # Check if moves form a rectangle
    return abs(move1 - move2) == 1 or abs(move1 - move2) == 4


def player_turn(player_number, board, squares_taken):
    # make each player turn
    print(f"Player {player_number}, please choose two squares: ")
    for row in board:
        print(row)
    while True:
        move1 = input("Enter first square number: ")
        move2 = input("Enter second square number: ")
        if move1.isdigit() and move2.isdigit():
            move1 = int(move1)
            move2 = int(move2)
            if 1 <= move1 <= 16 and 1 <= move2 <= 16 and move1 != move2:
                # Check if both squares form a rectangle and are available
                if is_rectangle(move1, move2):
                    if move1 not in squares_taken and move2 not in squares_taken:
                        squares_taken.extend([move1, move2])
                        for row in board:
                            for i, square in enumerate(row):
                                if square == move1 or square == move2:
                                    row[i] = 'x'
                        break  # Exit the loop if the move is valid
                    else:
                        print("One or both of the selected squares are already taken. Please choose again.")
                else:
                    print("The selected squares do not form a rectangle, please choose again.")
            else:
                print("Please enter valid square numbers.")
        else:
            print("Please enter valid integers.")


def check_draw(board):
    # Check if the game has ended in a draw.
    return not any(square != 'x' for row in board for square in row)


def main():
    # Initialize the game board and other variables
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    squares_taken = []  # Initialize list to keep track of taken squares

    print("Welcome to my Two Squares game")

    while True:
        # Player 1's turn
        player_turn(1, board, squares_taken)
        if check_draw(board):
            print("The game ends in a draw.")
            break
        if not can_play(board):
            print("Player 1 wins!")
            break

        # Player 2's turn
        player_turn(2, board, squares_taken)
        if check_draw(board):
            print("The game ends in a draw.")
            break
        if not can_play(board):
            print("Player 2 wins!")
            break


main()
