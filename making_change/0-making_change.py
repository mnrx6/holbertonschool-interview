#!/usr/bin/python3
"""Minimum number of coins to make change."""


def makeChange(coins, total):
    """Return the minimum number of coins needed to make change."""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for num in range(1, total + 1):
        for coin in coins:
            if coin <= num:
                dp[num] = min(dp[num], dp[num - coin] + 1)

    if dp[total] == total + 1:
        return -1

    return dp[total]
