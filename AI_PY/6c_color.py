import matplotlib.pyplot as plt
import networkx as nx

def is_valid(state, color, neighbor_map, assignment):
    for neighbor in neighbor_map[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, states, colors, neighbor_map):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment]
    state = unassigned[0]

    for color in colors:
        if is_valid(state, color, neighbor_map, assignment):
            assignment[state] = color
            result = backtrack(assignment, states, colors, neighbor_map)
            if result:
                return result
            del assignment[state]
    return None

# States and their neighbors
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbor_map = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# New colors for the states
colors = ['RED', 'GREEN', 'BLUE']

# Find solution using backtracking
solution = backtrack({}, states, colors, neighbor_map)

# Print the result
print("Map Coloring Solution:")
print(solution)

# Create a graph for visualization
G = nx.Graph()

# Add states as nodes and edges based on the neighbor map
for state, neighbors in neighbor_map.items():
    for neighbor in neighbors:
        G.add_edge(state, neighbor)

# Assign colors to the nodes based on the solution
node_colors = [solution[state] if state in solution else 'gray' for state in G.nodes()]

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Layout for the nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, font_size=12, font_weight='bold', edge_color='gray')

# Display the map with colored states
plt.title("Map Coloring Solution")
plt.show()