#!/usr/bin/python3
"""A program to solve the N queens problem"""

import sys


def print_solution(board):
    """Prints the board in a specific format."""
    solution = []
    for row in board:
        solution.append(''.join('Q' if col else '.' for col in row))
    print('\n'.join(solution))


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    """Check this column on the upper side"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    """Check upper diagonal on the left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j] == 1:
            return False

    """Check upper diagonal on the right side"""
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):
            break
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row):
    """Utilizes backtracking to solve the N-Queens problem."""
    if row >= len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            """Place queen"""
            board[row][col] = 1
            """Recur to place rest of the queens"""
            solve_nqueens_util(board, row + 1)
            """Backtrack"""
            board[row][col] = 0


def solve_nqueens(N):
    """Initializes the board and starts the solving process."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
