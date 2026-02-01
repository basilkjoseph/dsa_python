def bellman_ford(edges, n, source):
    """
    Compute shortest paths from a single source to all vertices using Bellman-Ford algorithm.

    Parameters:
    - edges: list of tuples (u, v, weight) representing directed edges
    - n: number of vertices (vertices are assumed to be 0..n-1)
    - source: index of the starting vertex

    Returns:
    - dist: list of distances where dist[i] is the shortest distance from source to i
            (float('inf') if a vertex is unreachable)

    Raises:
    - ValueError: if the graph contains a negative weight cycle reachable from the source

    Time complexity: O(V * E)
    Space complexity: O(V)
    """
    # Initialize distances with 'infinity' and set source distance to 0
    dist = [float('inf')] * n
    dist[source] = 0

    # Relax all edges up to V-1 times. After k iterations, shortest paths using at most k edges
    # are guaranteed to be found. This is the core of the Bellman-Ford algorithm.
    for _ in range(n - 1):
        for u, v, w in edges:
            # Only consider relaxation if the source vertex of the edge is reachable
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                # Update the distance to v if a shorter path via u is found
                dist[v] = dist[u] + w

    # One more iteration: if any distance can still be relaxed, there exists a negative
    # weight cycle reachable from the source. In that case, shortest paths are undefined.
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
