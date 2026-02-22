from typing import List

class Solution:
    def dfs(self,node,paths,graph):
        if paths[node]==[-1]:
            paths[node]=[]
            for child in graph[node]:
                subs_path=self.dfs(child,paths,graph)
                for sp in subs_path:
                    paths[node].append([node]+sp)
        return paths[node]


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n=len(graph)
        paths=[[-1] for _ in range(n)]
        self.dfs(0,paths,graph)
        return paths[0]
        