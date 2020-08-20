import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline())
    
    stuff = list()
    for _ in range(N):
        W, V = map(int, sys.stdin.readline())
        stuff.append([W, V])
    
    dp = [[0 for i in range(K + 1)] for j in range(N + 1)]
    
    for i in range(1, N + 1):
        weight, value = 