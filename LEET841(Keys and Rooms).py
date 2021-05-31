from typing import List
from collections import deque

class Solution:
    def dfs(self, x, rooms):
        global visited
        
        visited[x] = 1
        
        for room in rooms[x]:
            if visited[room] == 0:
                self.dfs(room, rooms)

    def bfs(self, queue, rooms):
        global visited

        while queue:
            item = queue.popleft()
            visited[item] = 1
            for room in rooms[item]:
                if visited[room] == 0:
                    queue.append(room)
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        global visited
        
        N = len(rooms)
        
        visited = [0] * N
        
        self.dfs(0, rooms)

        queue = deque([0])
        self.bfs(queue, rooms)
        
        return all(visited)