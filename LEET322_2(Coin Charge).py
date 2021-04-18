from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1

        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min(dp[i - coin] if coin <= i else MAX for coin in coins) + 1

        return dp[amount] if dp[amount] < MAX else -1