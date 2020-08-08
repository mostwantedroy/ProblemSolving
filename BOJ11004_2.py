# 2. Using Heap

import sys
import heapq

if __name__ == "__main__":
    N, K = sys.stdin.readline().split(' ')
    N = int(N)
    K = int(K)
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    numbers.sort()
    heapq.heapify(numbers)
    for i in range(K):
        kth_min = heapq.heappop(numbers)
    print(kth_min)