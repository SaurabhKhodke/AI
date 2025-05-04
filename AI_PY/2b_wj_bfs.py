from collections import deque

def is_goal(state, target):
    a, b = state
    return a == target or b == target

def bfs(max_a, max_b, target):
    visited = set()
    # Queue stores tuples of (current_state, path_to_this_state)
    queue = deque([((0, 0), [(0, 0)])]) # Start with empty jugs

    print(f"Starting BFS for A={max_a}L, B={max_b}L, Target={target}L")

    while queue:
        (a, b), path = queue.popleft() # Get the oldest state from the queue

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if is_goal((a, b), target):
            print("\nReached goal!")
            # Print the path
            for step in path:
                print(f"-> A:{step[0]}L, B:{step[1]}L")
            return True

        # Define possible next states (operations)
        next_states = [
            (max_a, b),                         # Fill A
            (a, max_b),                         # Fill B
            (0, b),                             # Empty A
            (a, 0),                             # Empty B
            (a - min(a, max_b - b), b + min(a, max_b - b)), # Pour A -> B
            (a + min(b, max_a - a), b - min(b, max_a - a))  # Pour B -> A
        ]

        # Add valid, unvisited next states to the queue
        for state in next_states:
             # Basic check to ensure states are within bounds (optional but good practice)
             if 0 <= state[0] <= max_a and 0 <= state[1] <= max_b and state not in visited:
                 # Append the new state and the updated path
                queue.append((state, path + [state]))

    print("No solution found.")
    return False

# --- Main execution with User Input ---

# Get user input
max_a_input = input("Enter maximum capacity of Jug A: ")
max_b_input = input("Enter maximum capacity of Jug B: ")
target_input = input("Enter the target amount: ")

# Convert inputs to integers (assuming valid integer input for simplicity)
MAX_A = int(max_a_input)
MAX_B = int(max_b_input)
GOAL = int(target_input)

# Run BFS with user inputs
bfs(MAX_A, MAX_B, GOAL)