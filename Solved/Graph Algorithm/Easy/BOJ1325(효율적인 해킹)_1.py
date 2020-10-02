import sys
from collections import deque

def bfs(start):
    visited = [False] * (N + 1)

    need_visit = deque([start])
    visited[start] = True
    count = 1

    while need_visit:
        node = need_visit.popleft()
        for dest in network[node]:
            if not visited[dest]:
                need_visit.append(dest)
                visited[dest] = True
                count += 1
    
    return count

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    
    network = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        network[B].append(A)

    count = list()
    max_count = 0
    for i in range(1, N + 1):
        temp = bfs(i)
        if temp > max_count:
            max_count = temp
            count = [i]
        elif temp == max_count:
            count.append(i)
    
    for item in count:
        print(item, end = " ")