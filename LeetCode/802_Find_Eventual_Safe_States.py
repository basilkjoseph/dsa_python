from typing import List

class Solution:
    def dfs(self, graph, visited, node, curr_stack):
        """
        Depth-First Search to detect cycles in the graph.
        Args:
            graph: Adjacency list of the graph.
            visited: List to keep track of visited nodes.
            node: Current node being visited.
            curr_stack: List to keep track of nodes in the current DFS path (recursion stack).
        Returns:
            True if no cycle is detected from this node, False otherwise.
        """
        visited[node] = True
        curr_stack[node] = True  # Mark node as part of current DFS path

        for neighbor in graph[node]:
            if visited[neighbor]:
                # If neighbor is in current path, a cycle is detected
                if curr_stack[neighbor]:
                    return False
            # If neighbor is not visited, recursively visit it
            elif not self.dfs(graph, visited, neighbor, curr_stack):
                return False

        curr_stack[node] = False  # Remove node from current DFS path
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Finds all eventual safe nodes in a directed graph.
        An eventual safe node is a node from which all possible paths lead to a terminal node (no cycles).
        Args:
            graph: Adjacency list of the graph.
        Returns:
            List of safe node indices in ascending order.
        """
        visited = [False] * len(graph)      # Tracks if a node has been visited
        curr_stack = [False] * len(graph)   # Tracks nodes in the current DFS path
        result = []

        # Run DFS for each node to detect cycles
        for i in range(len(graph)):
            if not visited[i]:
                self.dfs(graph, visited, i, curr_stack)

        # Nodes not in any cycle (not in curr_stack) are safe
        for i in range(len(curr_stack)):
            if not curr_stack[i]:
                result.append(i)
        return result