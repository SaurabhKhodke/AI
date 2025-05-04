import heapq
import matplotlib.pyplot as plt
import networkx as nx

def a_star(cities, start, goal, heuristics):
    heap = [(heuristics[start], start, [start], 0)]
    visited = set()
    
    while heap:
        f, current, path, g = heapq.heappop(heap)
        
        if current == goal:
            return path, g
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, distance in cities.get(current, []):
            if neighbor not in visited:
                new_g = g + distance
                heapq.heappush(
                    heap,
                    (new_g + heuristics[neighbor],
                     neighbor,
                     path + [neighbor],
                     new_g)
                )
    
    return None, float('inf')

def draw_graph(cities, path=None):
    G = nx.Graph()
    
    # Add edges
    for city in cities:
        for neighbor, dist in cities[city]:
            G.add_edge(city, neighbor, weight=dist)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Base graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("A* Path Visualization")
    plt.show()

# Example usage
if __name__ == "__main__":
    cities = {
        'A': [('B', 5), ('C', 10)],
        'B': [('A', 5), ('C', 3), ('D', 2)],
        'C': [('A', 10), ('B', 3), ('D', 1), ('E', 7)],
        'D': [('B', 2), ('C', 1), ('E', 2)],
        'E': [('C', 7), ('D', 2)]
    }

    heuristics = {
        'A': 10, 'B': 6, 'C': 5, 
        'D': 2, 'E': 0
    }

    start = 'A'
    goal = 'E'
    path, distance = a_star(cities, start, goal, heuristics)
    
    if path:
        print(f"Shortest path from {start} to {goal}:")
        print(" -> ".join(path))
        print(f"Total distance: {distance} km")
        draw_graph(cities, path)
    else:
        print("No path exists")