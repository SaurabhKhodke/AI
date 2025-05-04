#include <stdio.h>
#include <string.h>

#define SIZE 10

void display(char grid[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++)
            printf("%c ", grid[i][j]);
        printf("\n");
    }
}

int can_place(char grid[SIZE][SIZE], char word[], int x, int y, int dir) {
    int len = strlen(word);

    if (dir == 0 && y + len > SIZE) return 0; // horizontal overflow
    if (dir == 1 && x + len > SIZE) return 0; // vertical overflow

    for (int i = 0; i < len; i++) {
        char existing = (dir == 0) ? grid[x][y+i] : grid[x+i][y];
        if (existing != '-' && existing != word[i]) return 0;
    }

    return 1;
}

void place_word(char grid[SIZE][SIZE], char word[], int x, int y, int dir) {
    int len = strlen(word);
    for (int i = 0; i < len; i++) {
        if (dir == 0)
            grid[x][y+i] = word[i];  // horizontal
        else
            grid[x+i][y] = word[i];  // vertical
    }
}

int main() {
    char grid[SIZE][SIZE];
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            grid[i][j] = '-';

    int n;
    printf("Enter number of words to insert: ");
    scanf("%d", &n);

    for (int w = 0; w < n; w++) {
        char word[20];
        int x, y, dir;

        printf("\nEnter word %d: ", w + 1);
        scanf("%s", word);
        printf("Enter start position (row col): ");
        scanf("%d %d", &x, &y);
        printf("Direction (0 = horizontal, 1 = vertical): ");
        scanf("%d", &dir);

        if (can_place(grid, word, x, y, dir)) {
            place_word(grid, word, x, y, dir);
        } else {
            printf("❌ Cannot place '%s' at (%d,%d) in that direction.\n", word, x, y);
            w--; // retry same word
        }
    }

    printf("\n✅ Final Crossword Grid:\n");
    display(grid);
    return 0;
}
