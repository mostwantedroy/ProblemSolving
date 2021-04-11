from typing import List

class Solution:
    def __init__(self):
        self.dp = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.make_dp(amount)
        self.dp[0] = 0

        num_coins = len(coins)

        for i in range(1, amount + 1):
            min_count = self.find_min_count(i, coins, num_coins)
            if min_count != -1:
                self.dp[i] = min_count + 1
            else:
                self.dp[i] = min_count

        print(self.dp)

        return self.dp[amount]

    def find_min_count(self, amount, coins, num_coins):

        params = [ amount for _ in range(num_coins) ]
        params = [ amount - coin for amount, coin in zip(params, coins)]

        temp = 9 * 10 ** 9
        for param in params:
            if param >= 0 and self.dp[param] > -1 and self.dp[param] < temp:
                temp = self.dp[param]

        if temp == 9 * 10 ** 9:
            temp = -1

        return temp

    def make_dp(self, amount):
        self.dp = [ -1 for i in range(amount + 1) ]

a = Solution()
print(a.coinChange([2, 3, 5], 11))