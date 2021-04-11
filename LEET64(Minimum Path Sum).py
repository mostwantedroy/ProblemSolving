class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        dp = [[0] * N for _ in range(M)]

        dp[0][0] = grid[0][0]

        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1] 
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j] 
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[M - 1][N - 1]