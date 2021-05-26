class Solution:
    def dfs(self, y, x, grid):
        global visited
        global M
        global N
        
        if 0 <= y < M and 0 <= x < N and grid[y][x] == 1 and visited[y][x] == 0:
            visited[y][x] = 1
            return 1 + self.dfs(y - 1, x, grid) + self.dfs(y, x - 1, grid) + self.dfs(y + 1, x, grid) + self.dfs(y, x + 1, grid)
        else:
            return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global visited
        global M
        global N
        
        M = len(grid)
        N = len(grid[0])
        
        visited = [[0] * N for _ in range(M)]
        
        max_area = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = self.dfs(i, j, grid)
                    max_area = max(max_area, area)
                    
        return max_area