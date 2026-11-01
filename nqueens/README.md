# N Queens

## Description

This project solves the N Queens problem using the Backtracking algorithm in Python.

The goal is to place N queens on an N×N chessboard so that no two queens can attack each other.

## Requirements

- Python 3
- Only the `sys` module is allowed.
- N must be an integer greater than or equal to 4.

## Usage

```bash
./0-nqueens.py N
```

## Example

```bash
./0-nqueens.py 4
```

Output:

```text
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Algorithm

The program uses Backtracking to find all possible solutions.

1. Place a queen in a safe position.
2. Move to the next row.
3. Check for conflicts with other queens.
4. If necessary, remove the queen and try another position.
5. Print every valid solution.

## File

- `0-nqueens.py`: Solves the N Queens problem.

