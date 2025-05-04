import heapq
from copy import deepcopy

# Goal state
GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Moves: Left, Right, Up, Down
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

class Node:
    def __init__(self, puzzle, x, y, depth, parent, heuristic):
        self.puzzle = puzzle
        self.x = x  # Blank tile row
        self.y = y  # Blank tile column
        self.depth = depth
        self.parent = parent
        self.heuristic = heuristic

    # Required for heapq to compare nodes
    def __lt__(self, other):
        return self.heuristic < other.heuristic

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_row = (puzzle[i][j] - 1) // 3
                goal_col = (puzzle[i][j] - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def best_first_search(start, x, y):
    heap = []
    initial_heuristic = manhattan_distance(start)
    root = Node(start, x, y, 0, None, initial_heuristic)
    heapq.heappush(heap, root)

    visited = set()

    while heap:
        current = heapq.heappop(heap)
        puzzle_tuple = tuple(tuple(row) for row in current.puzzle)

        if puzzle_tuple in visited:
            continue
        visited.add(puzzle_tuple)

        if current.puzzle == GOAL:
            print(f"Solution found at depth: {current.depth}")
            print_solution(current)
            return True

        for i in range(4):
            new_x = current.x + dx[i]
            new_y = current.y + dy[i]

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_puzzle = deepcopy(current.puzzle)
                new_puzzle[current.x][current.y], new_puzzle[new_x][new_y] = new_puzzle[new_x][new_y], new_puzzle[current.x][current.y]
                heuristic = manhattan_distance(new_puzzle)
                child = Node(new_puzzle, new_x, new_y, current.depth + 1, current, heuristic)
                heapq.heappush(heap, child)

    return False

def print_solution(node):
    if node is None:
        return
    print_solution(node.parent)
    for row in node.puzzle:
        print(" ".join(str(cell) for cell in row))
    print()

if __name__ == "__main__":
    print("Enter the initial puzzle configuration (9 numbers from 0 to 8, separated by spaces):")
    try:
        entries = list(map(int, input().strip().split()))
        if sorted(entries) != list(range(9)):
            raise ValueError("Input must contain all digits from 0 to 8 exactly once.")
        start = [entries[i:i+3] for i in range(0, 9, 3)]

        # Find initial blank (0) position
        x, y = next((i, j) for i in range(3) for j in range(3) if start[i][j] == 0)

        if not best_first_search(start, x, y):
            print("No solution found!")
    except Exception as e:
        print(f"Invalid input: {e}")
