import sys
import heapq

def dijkstra(start):
    heap = list()

    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        time, node = heapq.heappop(heap)
        if distance[node] < time:
            continue
        for dest in network[node]:
            time_new = time + dest[0]
            if distance[dest[1]] > time_new:
                distance[dest[1]] = time_new
                heapq.heappush(heap, (time_new, dest[1]))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for t in range(T):
        N, D, C = map(int, sys.stdin.readline().split())
        
        network = [[] for _ in range(N + 1)]
        distance = [10 ** 9] * (N + 1)

        for _ in range(D):
            A, B, S = map(int, sys.stdin.readline().split())
            network[B].append((S, A))

        dijkstra(C)
        count = 0
        max_time = 0

        for time in distance:
            if time != 10 ** 9:
                count += 1
                if time > max_time:
                    max_time = time
        
        print(count, max_time)