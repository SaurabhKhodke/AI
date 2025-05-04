#include <stdio.h>

#define MAX 99

// Function to generate an odd-order magic square
void generateMagicSquare(int n) {
    int magic[MAX][MAX] = {0};

    int i = 0, j = n / 2, num;
    
    for (num = 1; num <= n * n; num++) {
        magic[i][j] = num;
        
        int newi = (i - 1 + n) % n;
        int newj = (j + 1) % n;

        if (magic[newi][newj] != 0) {
            i = (i + 1) % n;
        } else {
            i = newi;
            j = newj;
        }
    }

    printf("Magic Square of size %d:\n", n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%3d ", magic[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n;
    printf("Enter an odd number for Magic Square: ");
    scanf("%d", &n);

    if (n % 2 == 0 || n < 1 || n > MAX) {
        printf("Invalid input! Enter an odd number.\n");
        return 1;
    }

    generateMagicSquare(n);
    return 0;
}

