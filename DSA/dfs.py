from collections import deque, defaultdict

def dfs(graph, start):
    """
    Perform an iterative depth-first search (DFS) on a graph.
    Args:
        graph (dict): Adjacency list of the graph.
        start: The starting node for DFS.
    Returns:
        list: List of nodes in the order they were visited.
    """
    visited = set()
    stack = deque([start])
    order = []

    while stack:
        node = stack.pop()
        order.append(node)
        visited.add(node)
        # Only add unvisited neighbors to the stack
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    return order

# Example usage
if __name__ == "__main__":
    graph = defaultdict(list)
    graph[1] = [2, 3]
    graph[2] = [1, 8, 9]
    graph[3] = [1, 4, 5, 7]
    graph[4] = [3]
    graph[5] = [3]
    graph[7] = [3]
    graph[9] = [2]
    graph[8] = [2, 10]

    result = dfs(graph, 1)
    print("DFS order:", result)