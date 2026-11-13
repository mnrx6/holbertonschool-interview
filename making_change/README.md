
# Making Change

## Description
This project solves the Making Change problem using Dynamic Programming.

The goal is to find the minimum number of coins needed to make a given amount.

## Requirements
- Python 3
- Ubuntu 20.04
- PEP 8 style

## Files
- `0-making_change.py`: Contains the `makeChange(coins, total)` function.

## How It Works
- Returns `0` if the total is zero or negative.
- Returns the minimum number of coins needed.
- Returns `-1` if the total cannot be made.

## Example
```python
makeChange([1, 2, 25], 37)
# Output: 7
```

## Algorithm
Dynamic Programming

Time Complexity: O(total * len(coins))

Space Complexity: O(total)

