from typing import List

class Solution:
    def dfs(self,graph,node,visited):
        visited[node]=True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(graph,neighbor,visited)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        self.dfs(rooms,0,visited)
        for i in visited:
            if not i: 
                return False
        return True