# Rotate 2D Matrix

## Description
This project rotates an N x N 2D matrix 90 degrees clockwise using Python.

The matrix is modified in-place without returning a new matrix.

## Requirements
- Python 3
- The matrix must be square (N x N).
- The function must modify the original matrix.
- The function must not return anything.

## File
- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix(matrix)` function.

## Example

**Input:**
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Output:**
```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Algorithm
The matrix is rotated in two steps:

1. Transpose the matrix by swapping rows and columns.
2. Reverse each row to rotate the matrix 90 degrees clockwise.

## Usage
```bash
python3 main_0.py
```
