import sys

def check_possible(arr):
    length = len(arr)
    for i in range(length - 1, -1, -1):
        if arr[i]:
            return i
    return -1


if __name__ == "__main__":
    N, S, M = map(int, sys.stdin.readline().split())
    V = list(map(int, sys.stdin.readline().split()))
    
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = True
    for i in range(1, N + 1):
        for j in range(0, M + 1):
            if dp[i - 1][j]:
                if j - V[i - 1] >= 0:
                    dp[i][j - V[i - 1]] = True
                if j + V[i - 1] <= M:
                    dp[i][j + V[i - 1]] = True

    print(check_possible(dp[N]))