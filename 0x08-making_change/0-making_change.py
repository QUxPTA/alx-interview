#!/usr/bin/python3
"""
 Determine the fewest number of coins
 using dynamic programming
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of integers representing the coin denominations.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    # Initialize the DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
