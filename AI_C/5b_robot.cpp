#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ROW 5
#define COL 5

typedef struct {
    int x, y;
    int g; // cost so far
    int h; // heuristic (Manhattan)
    int f; // total cost f = g + h
} Node;

int goalX = 4, goalY = 4;

int grid[ROW][COL] = {
    {0, 0, 0, 1, 0},    
    {1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0},
    {0, 1, 1, 1, 1},
    {0, 0, 0, 0, 0}
};

int visited[ROW][COL] = {0};

// Manhattan Distance
int heuristic(int x, int y) {
    return abs(x - goalX) + abs(y - goalY);
}

void aStarSearch(int startX, int startY) {
    Node queue[100];
    int front = 0, rear = 0;

    Node start = {startX, startY, 0, heuristic(startX, startY), 0};
    start.f = start.g + start.h;
    queue[rear++] = start;
    visited[startX][startY] = 1;

    int dx[] = {-1, 1, 0, 0}; // directions: up, down
    int dy[] = {0, 0, -1, 1}; // directions: left, right

    while (front < rear) {
        Node current = queue[front++];
        printf("Robot at (%d, %d), f = %d, g = %d, h = %d\n", current.x, current.y, current.f, current.g, current.h);

        if (current.x == goalX && current.y == goalY) {
            printf("Reached Goal at (%d, %d) with total cost: %d\n", current.x, current.y, current.f);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];

            if (nx >= 0 && nx < ROW && ny >= 0 && ny < COL &&
                !visited[nx][ny] && grid[nx][ny] == 0) {

                Node next;
                next.x = nx;
                next.y = ny;
                next.g = current.g + 1;
                next.h = heuristic(nx, ny);
                next.f = next.g + next.h;
                visited[nx][ny] = 1;

                // insert sorted by f = g + h
                int pos = rear;
                while (pos > front && queue[pos - 1].f > next.f) {
                    queue[pos] = queue[pos - 1];
                    pos--;
                }
                queue[pos] = next;
                rear++;
            }
        }
    }

    printf("Path not found.\n");
}

int main() {
    aStarSearch(0, 0);
    return 0;
}
