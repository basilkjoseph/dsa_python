from typing import List


class Solution:
    def dfs(self,graph,node,paths,allPaths):
        paths.append(node)
        if node==len(graph)-1:
            allPaths.append(paths[:])
            return
        for child in graph[node]:
            self.dfs(graph,child,paths,allPaths)
            paths.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths=list()
        allPaths=list()
        self.dfs(graph,0,paths,allPaths)
        return allPaths


        