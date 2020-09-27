import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dp = [0 for i in range(N + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    print(dp[N])