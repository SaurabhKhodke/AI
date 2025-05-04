def generate_magic_square(n):
    if n % 2 == 0:
        print("Error: Only works for odd numbers.")
        return None

    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2 # Start at middle of top row

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        # Calculate the next position (up one, right one)
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j]: # Already filled move, down one from the current position
            i = (i + 1) % n
        else:
            i, j = new_i, new_j # If the calculated position is empty, move to it

    return magic_square

def print_magic_square(square):
    if square is None:
        return

    n = len(square)
    cell_width = len(str(n * n)) # For formatting

    for row in square:
        print(" ".join(f"{num:{cell_width}d}" for num in row))

def run_magic_square_generator():
    while True:
        try:
            n_input = input("Enter the size of the magic square (N - must be odd): ")
            n = int(n_input)
            if n <= 0:
                print("Please enter a positive integer.")
            elif n % 2 == 0:
                 print("Please enter an odd number.")
            else:
                break # Valid input
        except ValueError:
            print("Invalid input. Please enter an integer.")

    magic = generate_magic_square(n)

    if magic:
        print("\nGenerated Magic Square:")
        print_magic_square(magic)

run_magic_square_generator()