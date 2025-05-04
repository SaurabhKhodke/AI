#include <stdio.h>

#define N 4  // Number of regions
int graph[N][N] = {
    {0, 1, 1, 1},  // Region 0 connected to 1,2,3
    {1, 0, 1, 0},
    {1, 1, 0, 1},
    {1, 0, 1, 0}
};

int colors[N];

int is_valid(int node, int color) {
    for (int i = 0; i < N; i++) {
        if (graph[node][i] && colors[i] == color)
            return 0;
    }
    return 1;
}

int solve(int node, int m) {
    if (node == N)
        return 1;

    for (int c = 1; c <= m; c++) {
        if (is_valid(node, c)) {
            colors[node] = c;
            if (solve(node + 1, m))
                return 1;
            colors[node] = 0;
        }
    }
    return 0;
}

int main() {
    int m = 3;  // Number of colors
    if (solve(0, m)) {
        for (int i = 0; i < N; i++)
            printf("Region %d --> Color %d\n", i, colors[i]);
    } else {
        printf("No solution found.\n");
    }
    return 0;
}
