def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                board[i][j] = 'O'
                print(f"Computer (O) plays at position {3*i + j + 1}")
                return

def play_tic_tac_toe():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        if current_player == 'X':
            move = input("Player X, enter your move (1-9): ")
            moved = False
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = 'X'
                        moved = True
                        break
                if moved:
                    break
        else:
            computer_move(board)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

play_tic_tac_toe()