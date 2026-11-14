#!/usr/bin/python3
"""Making change: fewest coins needed to reach a total."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Return 0 if total is 0 or less, and -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    impossible = total + 1
    dp = [0] + [impossible] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != impossible else -1
