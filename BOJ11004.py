# 1. Straightforward method : sort and find k-1th element

import sys

if __name__ == "__main__":
    N, K = sys.stdin.readline().split(' ')
    N = int(N)
    K = int(K)
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    numbers.sort()
    print(numbers[K - 1])