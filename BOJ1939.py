import sys
from collections import deque

def bfs(start, end, weight):
    global N
    visited = [False] * (N + 1)
    need_visit = deque([start])
    visited[int(start)] = True
    
    while need_visit:
        node = need_visit.popleft()
        for key in graph[node]:
            if graph[node][key] < weight:
                continue
            elif not visited[int(key)]:
                need_visit.append(key)
                visited[int(key)] = True
    
    return visited[int(end)]


if __name__ == "__main__":
    N, M = map(int, list(sys.stdin.readline().split()))
    
    graph = dict()
    load_min = 10 ** 9
    load_max = 1
    for _ in range(M):
        A, B, C = sys.stdin.readline().split()
        C = int(C)
        if not A in graph:
            graph[A] = {B : C}
        else:
            graph[A][B] = C
        if not B in graph:
            graph[B] = {A : C}
        else:
            graph[B][A] = C
        
        if C > load_max:
            load_max = C
        if C < load_min:
            load_min = C
    
    Dest, Start = sys.stdin.readline().split()
    
    result = load_min
    while load_min <= load_max:
        mid = (load_min + load_max) // 2
        if bfs(Start, Dest, mid):
            result = mid
            load_min = mid + 1
        else:
            load_max = mid - 1
    print(result)