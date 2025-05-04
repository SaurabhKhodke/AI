import heapq

def a_star(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = []
    heapq.heappush(heap, (0, start[0], start[1], [start], 0))
    visited = set()

    while heap:
        _, row, col, path, g = heapq.heappop(heap)
        
        if (row, col) == goal:
            return path
        
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                new_g = g + 1
                h = abs(r - goal[0]) + abs(c - goal[1])
                heapq.heappush(heap, (new_g + h, r, c, path + [(r, c)], new_g))
    
    return None

def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print('*', end=' ')
            elif grid[i][j] == 1:
                print('1', end=' ')
            else:
                print('.', end=' ')
        print()

if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        grid = []

        print("Enter the grid row by row (0 for free, 1 for obstacle):")
        for i in range(rows):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            if len(row) != cols:
                raise ValueError("Incorrect number of columns")
            grid.append(row)

        start = tuple(map(int, input("Enter start position (row col): ").split()))
        goal = tuple(map(int, input("Enter goal position (row col): ").split()))

        if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
            raise ValueError("Start or goal is on an obstacle!")

        path = a_star(grid, start, goal)

        if path:
            print("\nPath found:")
            print_grid(grid, path)
            print("\nStep-by-step path:")
            for step, (r, c) in enumerate(path):
                print(f"Step {step}: ({r}, {c})")
        else:
            print("No path exists.")

    except Exception as e:
        print("Error:", e)
