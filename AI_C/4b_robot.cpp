#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ROW 5
#define COL 5

typedef struct {
    int x, y;
    int h; // heuristic
} Node;

int goalX = 4, goalY = 4;
int grid[ROW][COL] = {
    {0, 0, 0, 1, 0},
    {1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0},
    {0, 1, 1, 1, 1},
    {0, 0, 0, 1, 0}
};
int visited[ROW][COL];

int heuristic(int x, int y) {
    return abs(x - goalX) + abs(y - goalY);
}

void bestFirstSearch(int startX, int startY) {
    Node queue[100];
    int front = 0, rear = 0;
    queue[rear++] = (Node){startX, startY, heuristic(startX, startY)};
    visited[startX][startY] = 1;

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    while (front < rear) {
        Node current = queue[front++];
        printf("Robot at (%d, %d)\n", current.x, current.y);

        if (current.x == goalX && current.y == goalY) {
            printf("Reached Goal!\n");
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < ROW && ny < COL &&
                !visited[nx][ny] && grid[nx][ny] == 0) {

                Node next = {nx, ny, heuristic(nx, ny)};
                visited[nx][ny] = 1;

                // insert in queue based on heuristic
                int pos = rear;
                while (pos > front && queue[pos - 1].h > next.h) {
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
    bestFirstSearch(0, 0);
    return 0;
}
