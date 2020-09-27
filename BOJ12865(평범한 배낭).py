import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline())
    stuff = list()
    
    weight_min = 10**6
    for _ in range(N):
        W, V = map(int, sys.stdin.readline())
        stuff.append([W, V])
        if W < weight_min:
            weight_min = W
    
    stuff.sort(lambda x:(-x[1], x[0]))
    
    dp = [0 for _ in range(K)]
    dp[weight_min] = 
    for i in range(weight_min, K + 1):
        temp = 0
        while temp < weight_min:
            temp += 
        dp[i] = 
    
    
    stuff = list()
    for _ in range(N):
        W, V = map(int, sys.stdin.readline())
        stuff.append([W, V])
    
    dp = [[0 for i in range(K + 1)] for j in range(N + 1)]
    
    for i in range(1, N + 1):
        weight, value = 
