import sys
from collections import deque

def bfs(start, end):
    MAX = 100001

    time = [0] * MAX

    need_visit = deque([start])

    while need_visit:
        node = need_visit.popleft()
        if node == end:
            return time[node]
        for dest in (node - 1, node + 1, node * 2):
            if dest >= 0 and dest < MAX and not time[dest]:
                need_visit.append(dest)
                time[dest] = time[node] + 1

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    
    print(bfs(N, K))