class Solution:
    def dfs(self,graph,node,informTime):
        if informTime[node]==0:
            return 0
        max_time=0
        for neighbor in graph[node]:
            max_time=max(max_time,self.dfs(graph,neighbor,informTime))
        return max_time+informTime[node]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=[[] for _ in range(n)]
        for i,val in enumerate(manager):
            if val!=-1:
                graph[val].append(i)
        return self.dfs(graph,headID,informTime)