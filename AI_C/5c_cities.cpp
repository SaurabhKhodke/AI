#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>

#define MAX 5

typedef struct {
    char name[10];
    int x, y;         // Coordinates
    int heuristic;    // h(n), calculated at runtime
} City;

typedef struct {
    int adj[MAX][MAX];  // adjacency matrix (assume cost = 1 if connected)
    City cities[MAX];
    int n;
} Graph;

int visited[MAX];

// Get index of a city by name
int getIndex(Graph g, char *name) {
    for (int i = 0; i < g.n; i++)
        if (strcmp(g.cities[i].name, name) == 0)
            return i;
    return -1;
}


int calcHeuristic(City from, City to) {
    double dx = from.x - to.x;
    double dy = from.y - to.y;
    return (int)sqrt(dx * dx + dy * dy);
}

// A* Search function
void aStarSearch(Graph *g, char *startName, char *goalName) {
    int start = getIndex(*g, startName);
    int goal = getIndex(*g, goalName);

    // Calculate heuristic for all cities based on goal
    for (int i = 0; i < g->n; i++) {
        g->cities[i].heuristic = calcHeuristic(g->cities[i], g->cities[goal]);
    }

    int g_cost[MAX];  // g(n): cost from start
    int f_cost[MAX];  // f(n) = g + h
    int queue[MAX];
    int front = 0, rear = 0;

    for (int i = 0; i < g->n; i++) {
        visited[i] = 0;
        g_cost[i] = INT_MAX;
        f_cost[i] = INT_MAX;
    }

    g_cost[start] = 0;
    f_cost[start] = g->cities[start].heuristic;
    queue[rear++] = start;

    while (front < rear) {
        int current = queue[front++];
        printf("Visited: %s (f = %d, g = %d, h = %d)\n",
               g->cities[current].name, f_cost[current], g_cost[current], g->cities[current].heuristic);

        if (current == goal) {
            printf("Reached destination: %s\n", g->cities[goal].name);
            return;
        }

        for (int i = 0; i < g->n; i++) {
            if (g->adj[current][i]) {
                int temp_g = g_cost[current] + 1;  
                int temp_f = temp_g + g->cities[i].heuristic;

                if (!visited[i] || temp_f < f_cost[i]) {
                    visited[i] = 1;
                    g_cost[i] = temp_g;
                    f_cost[i] = temp_f;

                    // insert node i into queue sorted by f_cost
                    int pos = rear;
                    while (pos > front && f_cost[queue[pos - 1]] > f_cost[i]) {
                        queue[pos] = queue[pos - 1];
                        pos--;
                    }
                    queue[pos] = i;
                    rear++;
                }
            }
        }
    }

    printf("No path found.\n");
}

int main() {
    Graph g = {
        // Adjacency matrix
        {
            {0, 1, 1, 0, 0},  // A
            {1, 0, 1, 1, 0},  // B
            {1, 1, 0, 1, 1},  // C
            {0, 1, 1, 0, 1},  // D
            {0, 0, 1, 1, 0}   // E
        },
        // City names and coordinates (x, y)
        {
            {"A", 1, 1},
            {"B", 2, 2},
            {"C", 3, 1},
            {"D", 4, 2},
            {"E", 5, 1}
        },
        5
    };

    aStarSearch(&g, "A", "E");
    return 0;
}
