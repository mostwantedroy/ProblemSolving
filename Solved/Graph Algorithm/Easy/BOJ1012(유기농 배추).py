import sys

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
            if land[y + dy[i]][x + dx[i]] == 1 and not visited[y + dy[i]][x + dx[i]]:
                dfs(y + dy[i], x + dx[i])

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    T = int(sys.stdin.readline())
    
    for i in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        
        land = [[0] * M for _ in range(N)]
        
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            land[Y][X] = 1

        visited = [[False] * M for _ in range(N)]

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        count = 0
        for y in range(N):
            for x in range(M):
                if land[y][x] == 1 and not visited[y][x]:
                    dfs(y, x)
                    count += 1

        print(count)