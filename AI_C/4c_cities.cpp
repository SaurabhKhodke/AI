#include <stdio.h>
#include <string.h>

#define MAX 5

typedef struct {
    char name[10];
    int heuristic;
} City;

typedef struct {
    int adj[MAX][MAX];
    City cities[MAX];
    int n;
} Graph;

int visited[MAX];

int getIndex(Graph g, char *name) {
    for (int i = 0; i < g.n; i++)
        if (strcmp(g.cities[i].name, name) == 0)
            return i;
    return -1;
}

void bestFirstSearch(Graph g, char *startName, char *goalName) {
    int start = getIndex(g, startName);
    int goal = getIndex(g, goalName);

    int queue[MAX];
    int front = 0, rear = 0;
    queue[rear++] = start;
    visited[start] = 1;

    while (front < rear) {
        int current = queue[front++];
        printf("Visited: %s\n", g.cities[current].name);

        if (current == goal) {
            printf("Reached destination: %s\n", g.cities[goal].name);
            return;
        }

        for (int i = 0; i < g.n; i++) {
            if (g.adj[current][i] && !visited[i]) {
                visited[i] = 1;
                int pos = rear;
                while (pos > front && g.cities[queue[pos - 1]].heuristic > g.cities[i].heuristic) {
                    queue[pos] = queue[pos - 1];
                    pos--;
                }
                queue[pos] = i;
                rear++;
            }
        }
    }

    printf("No path found.\n");
}

int main() {
    Graph g = {
        {
            {0, 1, 1, 0, 0},
            {1, 0, 1, 1, 0},
            {1, 1, 0, 1, 1},
            {0, 1, 1, 0, 1},
            {0, 0, 1, 1, 0}
        },
        {
            {"A", 10},
            {"B", 8},
            {"C", 5},
            {"D", 7},
            {"E", 0}
        },
        5
    };

    bestFirstSearch(g, "A", "E");
    return 0;
}
