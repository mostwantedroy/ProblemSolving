import sys

def bfs(graph, start, mid):
    visited = list()
    need_visit = list()
    
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop(0)
        if node in graph:
            for key, value in graph[node]:
                if value > mid:
                    continue
                else:
                    need_visit.append()


if __name__ == "__main__":
    N, M = list(map(int, list(sys.stdin.readline().split(" "))))
    
    bridges = []
    graph = dict()
    load_min = 10 ** 9
    load_max = 1
    for _ in range(M):
        A, B, C = list(map(int, list(sys.stdin.readline().split(" "))))
        if (not A in graph) or (not B in graph):
            graph[A] = {B : C}
            graph[B] = {A : C}
        else:
            graph[A][B] = C
            graph[B][A] = C

        if C > load_max:
            load_max = C
        if C < load_min:
            load_min = C
    
    Dest, Start = list(map(int, list(sys.stdin.readline().split(" "))))

    while load_min <= load_max:
        mid = (load_min + load_max) // 2
        



    print(graph)