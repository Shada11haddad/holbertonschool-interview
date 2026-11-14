# Making Change

Given a list of coin values and a `total`, `makeChange(coins, total)` returns
the fewest number of coins needed to make that total.

- Returns `0` if `total` is 0 or less
- Returns `-1` if the total cannot be made with the given coins
- Each coin can be used an unlimited number of times

## Approach

Dynamic programming (bottom-up). `dp[a]` holds the fewest coins needed for
amount `a`. Starting from `dp[0] = 0`, each coin updates every amount it can
reach: `dp[a] = min(dp[a], dp[a - coin] + 1)`.

Time complexity: O(len(coins) * total). Space: O(total).
