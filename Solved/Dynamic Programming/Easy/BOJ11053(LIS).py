import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [1 for _ in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    
    print(max(dp))