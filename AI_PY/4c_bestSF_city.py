import heapq
import matplotlib.pyplot as plt
import networkx as nx

class CityGraph:
    def __init__(self):
        self.graph = {}
        self.heuristic = {}

    def add_edge(self, city1, city2, distance):
        self.graph.setdefault(city1, []).append((city2, distance))
        self.graph.setdefault(city2, []).append((city1, distance))

    def set_heuristic(self, city, value):
        self.heuristic[city] = value

    def best_first_search(self, start, goal):
        visited = set()
        heap = [(self.heuristic.get(start, float('inf')), start, [start], 0)]

        while heap:
            _, current, path, cost = heapq.heappop(heap)

            if current == goal:
                return path, cost

            if current in visited:
                continue
            visited.add(current)

            for neighbor, distance in self.graph.get(current, []):
                if neighbor not in visited:
                    new_cost = cost + distance
                    heapq.heappush(
                        heap,
                        (self.heuristic.get(neighbor, float('inf')),
                         neighbor,
                         path + [neighbor],
                         new_cost)
                    )

        return None, float('inf')

    def draw_graph(self, path=None):
        G = nx.Graph()
        for city in self.graph:
            for neighbor, distance in self.graph[city]:
                G.add_edge(city, neighbor, weight=distance)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=600, node_color='lightblue', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight path if provided
        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("City Graph with Best-First Path")
        plt.show()

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    graph = CityGraph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 10)
    graph.add_edge("B", "D", 3)
    graph.add_edge("C", "D", 2)
    graph.add_edge("D", "E", 4)
    graph.add_edge("B", "E", 9)

    graph.set_heuristic("A", 10)
    graph.set_heuristic("B", 6)
    graph.set_heuristic("C", 5)
    graph.set_heuristic("D", 2)
    graph.set_heuristic("E", 0)

    path, total_distance = graph.best_first_search("A", "E")

    if path:
        print("Path:", " -> ".join(path))
        print("Total Distance:", total_distance, "km")
        graph.draw_graph(path)
    else:
        print("No path found.")