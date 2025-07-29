from typing import List
from collections import deque

class Solution:
    """
    Solution class to find the number of provinces (connected components) in an undirected graph
    represented by an adjacency matrix.
    """

    def dfs(self, graph: List[List[int]], node: int, visited: set) -> None:
        """
        Depth-First Search (DFS) helper function to traverse all nodes in a province.

        Args:
            graph (List[List[int]]): The adjacency matrix representing the graph.
            node (int): The current node being visited.
            visited (set): Set of already visited nodes.
        """
        if node in visited:
            return
        visited.add(node)
        for j in range(len(graph)):
            if node != j and graph[node][j] == 1:
                self.dfs(graph, j, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Finds the number of provinces (connected components) in the given graph.

        Args:
            isConnected (List[List[int]]): The adjacency matrix representing the graph.

        Returns:
            int: The number of provinces.
        """
        visited = set()
        count = 0
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(isConnected, i, visited)
        return count



