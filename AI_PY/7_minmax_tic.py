import math
board = [[' ' for _ in range(3)] for _ in range(3)]
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_draw(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def best_move():
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'O'
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are 'X', computer is 'O'.")
    print_board()
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'

        print_board()
        if check_winner(board) == 'X':
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("Computer's turn:")
        best_move()
        print_board()
        if check_winner(board) == 'O':
            print("Computer wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play_game()