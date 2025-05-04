def print_solution(board):
    for row in board:
        # Print 'Q' for queen (1), '.' for empty (0)
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1: return False

    # Check upper-left diagonal
    for i in range(row):
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1: return False

    # Check upper-right diagonal
    for i in range(row):
        if col + (row - i) < n and board[i][col + (row - i)] == 1: return False

    return True

def solve_n_queens(board, row, n):
    # Base case: If all queens placed
    if row == n:
        print_solution(board)
        return

    # Try placing queen in each column of the current row
    for col in range(n):
        # If safe, place queen and recurse
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            # Backtrack: Remove queen to try other columns
            board[row][col] = 0

def n_queens():
    while True:
        try:
            n_input = input("Enter the size of the board (N): ")
            n = int(n_input)
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break # Valid input
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Initialize empty board
    board = [[0] * n for _ in range(n)]
    print(f"\nFinding solutions for N = {n}:")
    # Start solving from the first row (row 0)
    solve_n_queens(board, 0, n)
    print("Finished searching for solutions.")

n_queens()