def water_jug_dfs(max_a, max_b, target):
    visited = set()  # Keep track of states already visited to avoid cycles
    path = []        # Stores the sequence of states leading to the solution

    def dfs(a, b):
        # Base Case 1: Target reached
        if a == target or b == target:
            path.append((a, b)) # Add the final state to the path
            return True

        # Base Case 2: State already visited,prevents infinite loops.
        if (a, b) in visited:
            return False
        # Mark the current state as visited
        visited.add((a, b))
        # Add the current state to the potential solution path
        path.append((a, b))
        # Explore possible next states using recursive calls (DFS):
        # The order of these calls determines the search order.
        # 1. Fill Jug A
        if a < max_a and dfs(max_a, b):
            return True # Solution found down this path

        # 2. Fill Jug B
        if b < max_b and dfs(a, max_b):
            return True # Solution found down this path

        # 3. Empty Jug A
        if a > 0 and dfs(0, b):
            return True # Solution found down this path

        # 4. Empty Jug B
        if b > 0 and dfs(a, 0):
            return True # Solution found down this path

        # 5. Pour from A to B
        if a > 0 and b < max_b:
            pour = min(a, max_b - b) # Amount to pour
            if dfs(a - pour, b + pour):
                return True # Solution found down this path

        # 6. Pour from B to A
        if b > 0 and a < max_a:
            pour = min(b, max_a - a) # Amount to pour
            if dfs(a + pour, b - pour):
                return True # Solution found down this path

        # BACKTRACKING: If none of the operations from this state
        # led to the target, remove this state from the current path
        # and signal failure up the call stack.
        path.pop()
        return False

    # Start the DFS from the initial state (both jugs empty)
    if dfs(0, 0):
        print("\nSolution Path Found:")
        for state in path:
            print(f"Jug A: {state[0]}L, Jug B: {state[1]}L")
        return True
    else:
        print("\nNo solution exists for the given parameters.")
        return False

# --- Main execution with User Input ---
def run_water_jug_solver():
    while True:
        try:
            max_a = int(input("Enter the maximum capacity of Jug A: "))
            max_b = int(input("Enter the maximum capacity of Jug B: "))
            target = int(input("Enter the target amount: "))

        except ValueError:
            print("Invalid input. Please enter integers.")

        water_jug_dfs(max_a, max_b, target)

# Run the solver with user input
run_water_jug_solver()