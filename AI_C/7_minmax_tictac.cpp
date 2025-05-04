#include <stdio.h>
#include <limits.h>

char board[3][3];

// Function to initialize board
void initBoard() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = ' ';
}

// Function to print the board
void printBoard() {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf(" %c | %c | %c \n", board[i][0], board[i][1], board[i][2]);
        if (i < 2) printf("---|---|---\n");
    }
    printf("\n");
}

// Function to check winner
char checkWinner() {
    // Rows, Columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] &&
            board[i][1] == board[i][2] &&
            board[i][0] != ' ')
            return board[i][0];

        if (board[0][i] == board[1][i] &&
            board[1][i] == board[2][i] &&
            board[0][i] != ' ')
            return board[0][i];
    }

    // Diagonals
    if (board[0][0] == board[1][1] &&
        board[1][1] == board[2][2] &&
        board[0][0] != ' ')
        return board[0][0];

    if (board[0][2] == board[1][1] &&
        board[1][1] == board[2][0] &&
        board[0][2] != ' ')
        return board[0][2];

    return ' ';
}

// Function to check if moves are left
int isMovesLeft() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ')
                return 1;
    return 0;
}

// Minimax function
int minimax(int isMax) {
    char winner = checkWinner();
    if (winner == 'O') return 10;
    if (winner == 'X') return -10;
    if (!isMovesLeft()) return 0;

    int best;
    if (isMax) {
        best = INT_MIN;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == ' ') {
                    board[i][j] = 'O';
                    best = (minimax(0) > best) ? minimax(0) : best;
                    board[i][j] = ' ';
                }
    } else {
        best = INT_MAX;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == ' ') {
                    board[i][j] = 'X';
                    best = (minimax(1) < best) ? minimax(1) : best;
                    board[i][j] = ' ';
                }
    }
    return best;
}

// Find best move for computer
void bestMove() {
    int bestVal = INT_MIN, row = -1, col = -1;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ') {
                board[i][j] = 'O';
                int moveVal = minimax(0);
                board[i][j] = ' ';
                if (moveVal > bestVal) {
                    row = i;
                    col = j;
                    bestVal = moveVal;
                }
            }
    board[row][col] = 'O';
}

// Main game loop
int main() {
    int x, y;
    initBoard();
    printBoard();

    while (1) {
        printf("Enter your move (row and col: 0, 1, 2): ");
        scanf("%d %d", &x, &y);
        if (board[x][y] != ' ') {
            printf("Invalid move! Try again.\n");
            continue;
        }
        board[x][y] = 'X';
        printBoard();

        if (checkWinner() == 'X') {
            printf("You win!\n");
            break;
        }
        if (!isMovesLeft()) {
            printf("It's a draw!\n");
            break;
        }

        printf("Computer's move:\n");
        bestMove();
        printBoard();

        if (checkWinner() == 'O') {
            printf("Computer wins!\n");
            break;
        }
        if (!isMovesLeft()) {
            printf("It's a draw!\n");
            break;
        }
    }
    return 0;
}
