#!/usr/bin/python3
"""determines the least number of coins to be returned for change"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
