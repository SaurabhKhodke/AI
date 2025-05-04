#include <stdio.h>

int CAP1, CAP2, goal;
int visited[100][100];

typedef struct {
    int jug1, jug2;
} State;

int dfs(State s) {
    if (visited[s.jug1][s.jug2]) return 0;
    visited[s.jug1][s.jug2] = 1;

    printf("Jug1: %d, Jug2: %d\n", s.jug1, s.jug2);
    
    // ✅ Check if goal is in Jug1, Jug2 or their total
    if (s.jug1 == goal) return 1;

    int pourToJug2 = (s.jug1 < (CAP2 - s.jug2)) ? s.jug1 : (CAP2 - s.jug2);
    int pourToJug1 = (s.jug2 < (CAP1 - s.jug1)) ? s.jug2 : (CAP1 - s.jug1);

    State moves[6] = {
        {CAP1, s.jug2},                               // Fill Jug1
        {s.jug1, CAP2},                               // Fill Jug2
        {0, s.jug2},                                  // Empty Jug1
        {s.jug1, 0},                                  // Empty Jug2
        {s.jug1 - pourToJug2, s.jug2 + pourToJug2},   // Pour Jug1 -> Jug2
        {s.jug1 + pourToJug1, s.jug2 - pourToJug1}    // Pour Jug2 -> Jug1
    };

    for (int i = 0; i < 6; i++) {
        if (dfs(moves[i])) return 1;
    }

    return 0;
}

int main() {
    printf("Enter capacity of Jug1: ");
    scanf("%d", &CAP1);
    printf("Enter capacity of Jug2: ");
    scanf("%d", &CAP2);
    printf("Enter target quantity: ");
    scanf("%d", &goal);

    State start = {0, 0};
    if (!dfs(start))
        printf("Solution not found.\n");

    return 0;
}
