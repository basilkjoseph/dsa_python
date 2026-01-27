def bellman_ford(edges, n, source):
    """
    edges: list of (u, v, weight)
    n: number of vertices
    source: starting node
    """
    dist = [float('inf')] * n
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
