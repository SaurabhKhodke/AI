#include <stdio.h>
#include <stdlib.h>

#define MAX 10  // Maximum board size

int board[MAX][MAX];

// Function to print the board
void printSolution(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%c ", board[i][j] ? 'Q' : '-');
        }
        printf("\n");
    }
    printf("\n");
}

// Function to check if placing a queen is safe
int isSafe(int row, int col, int n) {
    for (int i = 0; i < col; i++) {
        if (board[row][i]) return 0;
    }

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j]) return 0;
    }

    for (int i = row, j = col; i < n && j >= 0; i++, j--) {
        if (board[i][j]) return 0;
    }

    return 1;
}

// Function to solve N-Queens using Backtracking
int solveNQueens(int col, int n) {
    if (col >= n) {
        printSolution(n);
        return 1;
    }

    int foundSolution = 0;
    for (int i = 0; i < n; i++) {
        if (isSafe(i, col, n)) {
            board[i][col] = 1;
            foundSolution = solveNQueens(col + 1, n) || foundSolution;
            board[i][col] = 0;
        }
    }
    
    return foundSolution;
}

int main() {
    int n;
    printf("Enter number of Queens: ");
    scanf("%d", &n);

    if (n < 1 || n > MAX) {
        printf("Invalid board size.\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            board[i][j] = 0;

    if (!solveNQueens(0, n)) {
        printf("No solution exists.\n");
    }

    return 0;
}

