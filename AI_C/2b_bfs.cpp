#include <stdio.h>

int CAP1, CAP2, goal;
int visited[100][100];

typedef struct {
    int jug1, jug2;
} State;

State queue[10000];
int front = 0, rear = 0;

void enqueue(State s) { queue[rear++] = s; }
State dequeue() { return queue[front++]; }
int isEmpty() { return front == rear; }

void bfs() {
    State start = {0, 0};
    enqueue(start);

    while (!isEmpty()) {
        State curr = dequeue();
        if (visited[curr.jug1][curr.jug2]) continue;

        visited[curr.jug1][curr.jug2] = 1;
        printf("Jug1: %d, Jug2: %d\n", curr.jug1, curr.jug2);

        
        if (curr.jug1 == goal) return;

        int pourToJug2 = (curr.jug1 < (CAP2 - curr.jug2)) ? curr.jug1 : (CAP2 - curr.jug2);
        int pourToJug1 = (curr.jug2 < (CAP1 - curr.jug1)) ? curr.jug2 : (CAP1 - curr.jug1);

        State moves[6] = {
            {CAP1, curr.jug2},                               // Fill Jug1
            {curr.jug1, CAP2},                               // Fill Jug2
            {0, curr.jug2},                                  // Empty Jug1
            {curr.jug1, 0},                                  // Empty Jug2
            {curr.jug1 - pourToJug2, curr.jug2 + pourToJug2}, // Jug1 to Jug2
            {curr.jug1 + pourToJug1, curr.jug2 - pourToJug1}  // Jug2 to Jug1
        };

        for (int i = 0; i < 6; i++) {
            enqueue(moves[i]);
        }
    }

    printf("Solution not found.\n");
}

int main() {
    printf("Enter capacity of Jug1: ");
    scanf("%d", &CAP1);
    printf("Enter capacity of Jug2: ");
    scanf("%d", &CAP2);
    printf("Enter target quantity: ");
    scanf("%d", &goal);

    bfs();

    return 0;
}
