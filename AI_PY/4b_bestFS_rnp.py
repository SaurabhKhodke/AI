import heapq

def best_first_search(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = []
    heapq.heappush(heap, (0, start[0], start[1], [start]))
    visited = set()
    visited.add(start)

    while heap:
        _, row, col, path = heapq.heappop(heap)

        if (row, col) == goal:
            return path

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                grid[r][c] == 0 and (r, c) not in visited):
                heuristic = abs(r - goal[0]) + abs(c - goal[1])
                heapq.heappush(heap, (heuristic, r, c, path + [(r, c)]))
                visited.add((r, c))
    return None

if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows in the grid: "))
        cols = int(input("Enter number of columns in the grid: "))
        print(f"Enter the grid values row-wise (use 0 for free, 1 for obstacle):")

        grid = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").strip().split()))
            if len(row) != cols:
                raise ValueError("Each row must have the specified number of columns.")
            grid.append(row)

        start = tuple(map(int, input("Enter start position (row col): ").strip().split()))
        goal = tuple(map(int, input("Enter goal position (row col): ").strip().split()))

        if not (0 <= start[0] < rows and 0 <= start[1] < cols):
            raise ValueError("Start position out of grid bounds.")
        if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
            raise ValueError("Goal position out of grid bounds.")
        if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
            raise ValueError("Start or goal position is on an obstacle.")

        path = best_first_search(grid, start, goal)
        if path:
            print("Path found:")
            for step in path:
                print(step)
        else:
            print("No path exists.")
    except Exception as e:
        print(f"Error: {e}")
