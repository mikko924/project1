import random

def check_winner(board):
    winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8),
                           (0, 4, 8), (2, 4, 6)]

    for a, b, c in winning_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return True
    return False

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def make_move(board, letter, move):
    if board[move] == ' ':
        board[move] = letter
        return True
    return False

def game():
    turn = 'player'
    board = [' '] * 9
    print_board(board)

    while not check_winner(board):
        move = input(f"{turn}, enter your move (1-9): ")
        if make_move(board, 'X' if turn == 'player' else 'O', int(move) - 1):
            print_board(board)
            if turn == 'player':
                turn = 'computer'
            else:
                turn = 'player'
        else:
            print("Invalid move, try again.")

    print(f"{'Computer' if turn == 'player' else 'Player'} wins!")

if __name__ == "__main__":
    game()