import sys
from collections import deque

def dfs(node):
    global N
    global visited

    print(node, end = ' ')
    visited[node] = True
    if node in graph:
        for other in graph[node]:
            if not visited[other]:
                dfs(other)

def bfs(start):
    global N
    global visited
    need_visit = deque([start])
    
    while need_visit:
        node = need_visit.popleft()
        if not visited[node]:
            print(node, end = ' ')
            if node in graph:
                for dest in graph[node]:
                    if not visited[node]:
                        need_visit.append(dest)
            visited[node] = True

if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    
    graph = dict()
    
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())

        if not A in graph:
            graph[A] = [B]
        else:
            graph[A].append(B)
        
        if not B in graph:
            graph[B] = [A]
        else:
            graph[B].append(A)
    
    for key in graph.keys():
        graph[key].sort()

    visited = [False] * (N + 1)
    dfs(V)
    print()
    visited = [False] * (N + 1)
    bfs(V)