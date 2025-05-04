def print_grid(grid):
    print("\n╔" + "══" * len(grid[0]) + "╗")
    for row in grid:
        print("║", end=" ")
        for cell in row:
            print("█" if cell == '+' else cell if cell != '-' else " ", end=" ")
        print("║")
    print("╚" + "══" * len(grid[0]) + "╝")


def can_place(grid, word, direction, i, j):
    if direction == 'H':
        if j + len(word) > len(grid[0]):
            return False
        for k in range(len(word)):
            if grid[i][j + k] not in ['-', word[k]] or grid[i][j + k] == '+':
                return False
    else:  # Vertical
        if i + len(word) > len(grid):
            return False
        for k in range(len(word)):
            if grid[i + k][j] not in ['-', word[k]] or grid[i + k][j] == '+':
                return False
    return True


def place_word(grid, word, direction, i, j):
    placed = []
    for k in range(len(word)):
        x = i + k if direction == 'V' else i
        y = j + k if direction == 'H' else j
        if grid[x][y] == '-':
            grid[x][y] = word[k]
            placed.append((x, y))
    return placed


def try_place_word(grid, word):
    first_char = word[0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == first_char:
                if can_place(grid, word, 'H', i, j):
                    place_word(grid, word, 'H', i, j)
                    return True
                if can_place(grid, word, 'V', i, j):
                    place_word(grid, word, 'V', i, j)
                    return True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if can_place(grid, word, 'H', i, j):
                place_word(grid, word, 'H', i, j)
                return True
            if can_place(grid, word, 'V', i, j):
                place_word(grid, word, 'V', i, j)
                return True
    return False


def initialize_grid(rows, cols, blocked_cells):
    grid = [['-' for _ in range(cols)] for _ in range(rows)]
    for i, j in blocked_cells:
        if 0 <= i < rows and 0 <= j < cols:
            grid[i][j] = '+'
    return grid


# Example blocked cells
blocked_cells = [
    (1, 1), (1, 2), (1, 3),
    (3, 5), (4, 5), (5, 5),
    (7, 0), (7, 1), (7, 2),
    (8, 8), (8, 9), (9, 8)
]

# Main Execution
if __name__ == "__main__":
    grid_size = 10
    grid = initialize_grid(grid_size, grid_size, blocked_cells)

    print("🧩 Start entering your words one by one. Type 'DONE' when finished.")
    print_grid(grid)

    while True:
        word = input("\nEnter word: ").strip().upper()
        if word == "DONE":
            break
        if not word.isalpha():
            print("❌ Invalid word. Please enter alphabetic characters only.")
            continue
        if try_place_word(grid, word):
            print("✅ Word placed.")
        else:
            print("❌ Could not place word.")
        print_grid(grid)

    print("\n🎉 Final Crossword:")
    print_grid(grid)
