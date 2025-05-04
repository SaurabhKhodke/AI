import heapq

# Goal configuration
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Possible moves and how they shift the blank index
MOVES = {
    'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1
}

class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank = board.index(0)
        self.cost = depth + heuristic(board)

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(board):
    # Manhattan distance
    distance = 0
    for i, val in enumerate(board):
        if val != 0:
            goal_i = GOAL_STATE.index(val)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_i, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def is_solvable(board):
    inv = 0
    for i in range(8):
        for j in range(i+1, 9):
            if board[i] and board[j] and board[i] > board[j]:
                inv += 1
    return inv % 2 == 0

def a_star(start):
    if not is_solvable(start):
        return None

    open_list = []
    visited = set()
    heapq.heappush(open_list, PuzzleState(start))

    while open_list:
        state = heapq.heappop(open_list)

        if state.board == GOAL_STATE:
            return state

        visited.add(tuple(state.board))

        for move, delta in MOVES.items():
            new_blank = state.blank + delta
            if not is_valid_move(state.blank, move):
                continue

            new_board = state.board[:]
            new_board[state.blank], new_board[new_blank] = new_board[new_blank], new_board[state.blank]

            if tuple(new_board) in visited:
                continue

            heapq.heappush(open_list, PuzzleState(new_board, state, move, state.depth + 1))

    return None

def is_valid_move(pos, move):
    if move == 'Up' and pos < 3: return False
    if move == 'Down' and pos > 5: return False
    if move == 'Left' and pos % 3 == 0: return False
    if move == 'Right' and pos % 3 == 2: return False
    return True

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()

    for i, s in enumerate(path):
        print(f"Step {i}: {'Move ' + s.move if s.move else 'Initial'}")
        print_board(s.board)
    print(f"Total moves: {len(path) - 1}")

if __name__ == "__main__":
    try:
        inp = list(map(int, input("Enter 9 numbers (0-8) separated by space: ").split()))
        if sorted(inp) != list(range(9)):
            raise ValueError("Invalid input: must contain digits 0–8 exactly once.")
        solution = a_star(inp)
        if solution:
            print("Solution found!\n")
            print_solution(solution)
        else:
            print("No solution exists for this puzzle.")
    except Exception as e:
        print("Error:", e)

#1 2 3 4 5 6 7 8 0 goal
#1 2 3 4 0 6 7 5 8 start