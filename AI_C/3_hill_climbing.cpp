#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define N 3

typedef struct {
    int board[N][N];
    int x, y; 
    int cost; 
} State;

int goal[N][N] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int calculateHeuristic(int board[N][N]) {
    int misplaced = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] != 0 && board[i][j] != goal[i][j]) {
                misplaced++;
            }
        }
    }
    return misplaced;
}

void printBoard(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 0)
                printf(" _ ");
            else
                printf(" %d ", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int isValidMove(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N);
}

void copyBoard(int src[N][N], int dest[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

void hillClimbing(State start) {
    State current = start;
    current.cost = calculateHeuristic(current.board);

    while (current.cost > 0) {
        State next = current;
        int minCost = current.cost;
        
        for (int i = 0; i < 4; i++) {
            int newX = current.x + dx[i];
            int newY = current.y + dy[i];
            
            if (isValidMove(newX, newY)) {
                State neighbor = current;
                
                neighbor.board[current.x][current.y] = neighbor.board[newX][newY];
                neighbor.board[newX][newY] = 0;
                neighbor.x = newX;
                neighbor.y = newY;
                neighbor.cost = calculateHeuristic(neighbor.board);
                
                if (neighbor.cost < minCost) {
                    minCost = neighbor.cost;
                    next = neighbor;
                }
            }
        }
        
        if (next.cost >= current.cost) {
            printf("Stuck in a local optimum! No better moves available.\n");
            break;
        }
        
        current = next;
        printBoard(current.board);
    }
    
    if (current.cost == 0) {
        printf("Solution found!\n");
    }
}

int main() {
    State start = {
        {{1, 2, 3}, {4, 0, 6}, {7, 5, 8}}, 
        1, 1, 0 
    };
    
    printf("Initial State:\n");
    printBoard(start.board);
    
    printf("Solving using Hill Climbing:\n");
    hillClimbing(start);
    
    return 0;
}