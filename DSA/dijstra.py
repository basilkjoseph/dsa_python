import heapq

def dijkstra(graph, source):
    """
    graph: dict[int, list[tuple[int, int]]]
           adjacency list where graph[u] = [(v, weight), ...]
    source: starting node

    returns: dict[node] = shortest distance from source
    """
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    # Min-heap: (distance, node)
    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # Skip outdated entries
        if curr_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = curr_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
