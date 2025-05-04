#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 3

typedef struct {
    int mat[SIZE][SIZE];
    int x, y; // position of blank (0)
    int cost;
} Node;

int goal[SIZE][SIZE] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};

// Check if the current matrix is the goal state
int isGoal(int mat[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            if (mat[i][j] != goal[i][j])
                return 0;
    return 1;
}

// Heuristic: number of misplaced tiles
int calculateHeuristic(int mat[SIZE][SIZE]) {
    int h = 0;
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            if (mat[i][j] != 0 && mat[i][j] != goal[i][j])
                h++;
    return h;
}

// Copy one matrix to another
void copyMatrix(int src[SIZE][SIZE], int dest[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            dest[i][j] = src[i][j];
}

// Print a 3x3 matrix
void printMatrix(int mat[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++)
            printf("%d ", mat[i][j]);
        printf("\n");
    }
    printf("--------\n");
}

// Best First Search algorithm
void bestFirstSearch(Node start) {
    int dx[] = {-1, 1, 0, 0}; // directions: up, down, left, right
    int dy[] = {0, 0, -1, 1};

    Node queue[100];
    int front = 0, rear = 0;
    queue[rear++] = start;

    while (front < rear) {
        Node current = queue[front++];
        printMatrix(current.mat);

        if (isGoal(current.mat)) {
            printf("Goal reached!\n");
            return;
        }

        for (int k = 0; k < 4; k++) {
            int nx = current.x + dx[k];
            int ny = current.y + dy[k];

            if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE) {
                Node temp;
                copyMatrix(current.mat, temp.mat);
                temp.mat[current.x][current.y] = temp.mat[nx][ny];
                temp.mat[nx][ny] = 0;
                temp.x = nx;
                temp.y = ny;
                temp.cost = calculateHeuristic(temp.mat);

                // insert in sorted order by cost (Best First)
                int pos = rear;
                while (pos > front && queue[pos - 1].cost > temp.cost) {
                    queue[pos] = queue[pos - 1];
                    pos--;
                }
                queue[pos] = temp;
                rear++;
            }
        }
    }

    printf("Solution not found.\n");
}

// Main with user input
int main() {
    Node start;
    printf("Enter the 3x3 puzzle (use 0 for the blank tile):\n");

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            scanf("%d", &start.mat[i][j]);
            if (start.mat[i][j] == 0) {
                start.x = i;
                start.y = j;
            }
        }
    }

    start.cost = calculateHeuristic(start.mat);
    bestFirstSearch(start);
    return 0;
}
