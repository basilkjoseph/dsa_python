from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red_graph=[[] for _ in range(n)]
        for edge in redEdges:
            red_graph[edge[0]].append(edge[1])

        blue_graph=[[] for _ in range(n)]
        for edge in blueEdges:
            blue_graph[edge[0]].append(edge[1])

        visited=[False]*n
        red_dist=[401]*n
        blue_dist=[401]*n

        red_dist[0]=0
        blue_dist[0]=0

        queue=deque()
        queue.append(0)
        while queue:
            node=queue.popleft()
            visited[node]=True
            for neighbor in red_graph[node]:
                if visited[neighbor]==False:
                    queue.append(neighbor)
                if red_dist[neighbor]>blue_dist[node]+1:
                    red_dist[neighbor]=blue_dist[node]+1
                    if visited[neighbor]:
                        queue.append(neighbor)
                    #check for inserting in queue.
            
            for neighbor in blue_graph[node]:
                if visited[neighbor]==False:
                    queue.append(neighbor)
                if blue_dist[neighbor]>red_dist[node]+1:
                    blue_dist[neighbor]=red_dist[node]+1
                    if visited[neighbor]:
                        queue.append(neighbor)
                    #check for inserting in queue.
        result=list()
        for i in range(n):
            result.append(min(red_dist[i],blue_dist[i]))
        for i,val in enumerate(result):
            if val==401:
                result[i]=-1
        return result