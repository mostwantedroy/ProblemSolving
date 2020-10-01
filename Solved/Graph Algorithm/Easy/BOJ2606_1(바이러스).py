import sys

def dfs(start):
    global count
    visited[start] = True
    count += 1
    for node in graph[start]:
        if not visited[node]:
            dfs(node)
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

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

    count = 0
    
    visited = [False] * (N + 1)

    dfs(1)

    print(count - 1)