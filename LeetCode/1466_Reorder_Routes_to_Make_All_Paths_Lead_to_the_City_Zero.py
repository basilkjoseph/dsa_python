from typing import List

class Solution:
    # Depth-First Search to count edges that need to be reversed
    def dfs(self, node, graph_from, graph_to, visited):
        if visited[node] == 1:  # If already visited, return 0
            return 0
        visited[node] = 1       # Mark the node as visited
        count = 0

        # Traverse outgoing edges (original direction)
        for neighbor in graph_from[node]:
            if visited[neighbor] == 0:
                # Edge needs to be reversed, so increment count
                count = count + self.dfs(neighbor, graph_from, graph_to, visited) + 1

        # Traverse incoming edges (correct direction)
        for neighbor in graph_to[node]:
            count += self.dfs(neighbor, graph_from, graph_to, visited)

        return count

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Initialize adjacency lists
        graph_from = [[] for _ in range(n)]  # edges going from a node (i.e., need reversal)
        graph_to = [[] for _ in range(n)]    # edges coming to a node (correct direction)

        # Build the directed graph
        for pair in connections:
            fr = pair[0]
            to = pair[1]
            graph_from[fr].append(to)  # Store outgoing edge
            graph_to[to].append(fr)    # Store incoming edge

        visited = [0] * n  # Keep track of visited nodes
        return self.dfs(0, graph_from, graph_to, visited)  # Start DFS from node 0
