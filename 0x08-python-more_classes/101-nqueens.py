#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board, col, n, solutions):
    if col == n:
        solutions.append(list(board))
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_nqueens_util(board, col + 1, n, solutions)


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
