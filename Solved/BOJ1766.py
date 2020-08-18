import sys
import heapq

def topology_sort(graph, inDegree):
    queue = list()

    result = list()
    
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            heapq.heappush(queue, i)
    
    while queue:
        data = heapq.heappop(queue)
        result.append(data)
        for node in graph[data]:
            inDegree[node] -= 1
            if inDegree[node] == 0:
                heapq.heappush(queue, node)

    return result

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N + 1)]
    inDegree = [0 for i in range(N + 1)]
    
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        inDegree[B] += 1
    
    result = topology_sort(graph, inDegree)

    for i in result:
        print(i, end = ' ')