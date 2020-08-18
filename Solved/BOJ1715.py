import sys
import heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    cards = list()
    for _ in range(N):
        heapq.heappush(cards, int(sys.stdin.readline()))
    
    sum = 0
    for _ in range(N - 1):
        temp = heapq.heappop(cards) + heapq.heappop(cards)
        sum += temp
        heapq.heappush(cards, temp)
    
    print(sum)