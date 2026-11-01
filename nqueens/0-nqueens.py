#!/usr/bin/python3
"""N Queens problem."""

import sys


def is_allowed(board, row, col):
    """Check if a queen can be allowed to placed safely."""
    for a in board:
        if col == a[1]:
            return False
        if abs(row - a[0]) == abs(col - a[1]):
            return False
    return True


def place_queens(board, row, n):
    """Find all possible solutions using backtracking."""
    if n == row:
        print(board)
        return
    for col in range(n):
        if is_allowed(board, row, col):
            board.append([row, col])
            place_queens(board, row + 1, n)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    place_queens([], 0, n)
