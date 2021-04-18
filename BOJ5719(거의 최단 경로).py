import sys
import heapq

def dijkstra(start):
    heap = list()

    heapq.push(heap, route[start])
    distance[start] = 0

    while heap:
        node, dist = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for i in route[node]:
            dist_new = dist + i[0]
    

if __name__ == "__main__":
    while True:
        N, M = map(int, sys.stdin.readline().split())

        if N == 0 and M == 0:
            break

        S, D = map(int, sys.stdin.readline().split())

        route = [[] for _ in range(N)]
        distance = [10 ** 9] * N

        for _ in range(M):
            U, V, P = map(int, sys.stdin.readline())
            route[U].append((P, V))

        

        
            